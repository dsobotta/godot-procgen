# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

# Line too long
# pylint: disable=C0301

# Too few public methods OMEGALUL
# pylint: disable=R0903

import os
import pathlib
import bpy
from .. import core

class GenTerrain(core.buildstep.BuildStep):

    __base_name = ""
    __rel_path = ""
    __tmp_filepath = ""
    __chunks_x: int = 1
    __chunks_y: int = 1

    def __init__(self, operand: str, **kwargs):
        args = {
            'chunks_x': 5,
            'chunks_y': 5,
        }
        args.update(kwargs)

        self.__chunks_x = args["chunks_x"]
        self.__chunks_y = args["chunks_x"]
        self.__base_name = pathlib.Path(operand).stem
        rel_filename = os.path.relpath(operand, core.utils.get_source_dir())
        self.__rel_path = os.path.dirname(rel_filename)
        self.__tmp_filepath = core.utils.create_tmp_blend()

        core.utils.bl_open_file(operand)
        core.utils.bl_save_as_file(self.__tmp_filepath)

    def get_chunk_range(self, chunks: int) -> range:
        #center chunks around origin
        #odd n=5    --> [-2, -1, 0, 1, 2]
        #even n=4   -->     [-1, 0, 1, 2]
        cm1_over2: int = (chunks-1)/2
        cm1_mod2: int = (chunks-1)%2

        c_min: int = int(-cm1_over2)
        c_max: int = int(cm1_over2 + cm1_mod2)

        return range(c_min, c_max + 1)

    def run(self) -> bool:
        out_dir = os.path.join(core.utils.get_variants_dir(), self.__rel_path, self.__base_name)
        core.utils.create_dir(out_dir)

        seed_set = False
        shared_seed = 0

        for x in self.get_chunk_range(self.__chunks_x):
            for y in self.get_chunk_range(self.__chunks_y):
                #re-open temp file (before mesh conversion) so we don't have to spam undo operations
                core.utils.bl_open_file(self.__tmp_filepath)
                chunk_name = self.__base_name + "_x" + str(x) + "_y" + str(y)

                #https://blenderartists.org/t/bad-context-after-open-new-file-with-python/1398392
                for w in bpy.context.window_manager.windows:
                    s = w.screen
                    for a in s.areas:
                        if a.type == "VIEW_3D":
                            with bpy.context.temp_override(window=w, area=a):
                                bpy.ops.object.mode_set(mode='OBJECT')
                                bpy.ops.object.select_all(action='DESELECT')

                                for obj in bpy.data.objects:
                                    obj.select_set(True)
                                    for modifier in bpy.context.object.modifiers:
                                        if isinstance(modifier, bpy.types.NodesModifier):
                                            if not seed_set:
                                                shared_seed = core.reflection.randomize_input_byname(modifier, "Seed")
                                                seed_set = True
                                            else:
                                                core.reflection.set_input_by_name(modifier, "Seed", shared_seed)

                                            core.reflection.set_input_by_name(modifier, "GridX", x)
                                            core.reflection.set_input_by_name(modifier, "GridY", y)
                                            #core.reflection.print_inputs(modifier)

                                    obj.name = chunk_name + "_genobj"
                                    obj.data.name = "genmesh"
                                    bpy.ops.object.convert(target='MESH')

                                    path = os.path.join(out_dir, chunk_name + ".blend")
                                    core.utils.bl_save_as_file(path)
                                    #obj.select_set(False)
                                break

        self._cleanup()
        return True

    def _cleanup(self) -> None:
        pass
