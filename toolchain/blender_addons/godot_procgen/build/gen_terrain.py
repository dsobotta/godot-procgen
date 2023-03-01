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
import random
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

    def print_inputs(self, geo_node: bpy.types.NodesModifier):
        modifier_name = geo_node.name
        print("GDPG modifier: " + modifier_name)
        for node_input in geo_node.node_group.inputs:
            identifier = node_input.identifier
            is_int = isinstance(node_input, bpy.types.NodeSocketInterfaceInt)
            is_float = isinstance(node_input, bpy.types.NodeSocketInterfaceFloat)
            if is_int or is_float:
                value = bpy.context.object.modifiers[modifier_name].get(identifier)
                debug_data = [
                    node_input.name,
                    str(value)
                ]
                print(debug_data)

    def nsi_by_name(self, modifier: bpy.types.NodesModifier, input_name: str) -> bpy.types.NodeSocketInterface:
        for node_input in modifier.node_group.inputs:
            if input_name == node_input.name:
                return node_input
        return None

    # def get_input_by_name(self, modifier: bpy.types.NodesModifier, input_name: str, value):
    #     nsi = self.nsi_by_name(modifier, input_name)
    #     if nsi is None:
    #         print("Error, failed to find NodeSocketInterface with name: " + input_name)
    #         return 0

    #     return bpy.context.object.modifiers[modifier.name].get(nsi.identifier)

    #returns the value that was set
    def set_input_by_name(self, modifier: bpy.types.NodesModifier, input_name: str, value):
        nsi = self.nsi_by_name(modifier, input_name)
        if nsi is None:
            print("Error, failed to find NodeSocketInterface with name: " + input_name)
            return 0

        bpy.context.object.modifiers[modifier.name][nsi.identifier] = value
        return value

    #returns the value that was set
    def randomize_input_byname(self, modifier: bpy.types.NodesModifier, input_name: str):
        nsi = self.nsi_by_name(modifier, input_name)
        if nsi is None:
            print("Error, failed to find NodeSocketInterface with name: " + input_name)
            return 0
        return self.randomize_input(modifier, nsi)

    #returns the value that was set
    def randomize_input(self, modifier: bpy.types.NodesModifier, nsi: bpy.types.NodeSocketInterface):
        if isinstance(nsi, bpy.types.NodeSocketInterfaceInt):
            value = random.randrange(nsi.min_value, nsi.max_value)
            bpy.context.object.modifiers[modifier.name][nsi.identifier] = value
            return value
        if isinstance(nsi, bpy.types.NodeSocketInterfaceFloat):
            value = random.uniform(nsi.min_value, nsi.max_value)
            bpy.context.object.modifiers[modifier.name][nsi.identifier] = value
            return value
        return 0

    def run(self) -> bool:
        #center chunks around origin
        #odd n=5 --> [-2, -1, 0, 1, 2]
        #even n=4 --> [-1, 0, 1, 2]
        xm1_over2: int = (self.__chunks_x-1)/2
        xm1_mod2: int = (self.__chunks_x-1)%2
        ym1_over2: int = (self.__chunks_y-1)/2
        ym1_mod2: int = (self.__chunks_y-1)%2

        min_grid_x: int = int(-xm1_over2)
        max_grid_x: int = int(xm1_over2 + xm1_mod2)
        min_grid_y: int = int(-ym1_over2)
        max_grid_y: int = int(ym1_over2 + ym1_mod2)

        out_dir = os.path.join(core.utils.get_variants_dir(), self.__rel_path, self.__base_name)
        core.utils.create_dir(out_dir)

        seed_set = False
        shared_seed = 0

        for x in range(min_grid_x, max_grid_x + 1):
            for y in range(min_grid_y, max_grid_y + 1):
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
                                                shared_seed = self.randomize_input_byname(modifier, "Seed")
                                                seed_set = True
                                            else:
                                                self.set_input_by_name(modifier, "Seed", shared_seed)

                                            self.set_input_by_name(modifier, "GridX", x)
                                            self.set_input_by_name(modifier, "GridY", y)
                                            self.print_inputs(modifier)

                                    bpy.ops.object.convert(target='MESH')
                                    obj.name = chunk_name + "_genobj"
                                    obj.data.name = "genmesh"

                                    path = os.path.join(out_dir, chunk_name + ".blend")
                                    core.utils.bl_save_as_file(path)
                                    obj.select_set(False)
                                break

        self._cleanup()
        return True

    def _cleanup(self) -> None:
        pass
