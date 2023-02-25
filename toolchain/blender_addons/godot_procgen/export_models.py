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

import pathlib
import bpy
from . import utils
from . import build_step

class ExportModels(build_step.BuildStep):

    __base_name = ""

    def __init__(self, operand: str):
        self.__base_name = pathlib.Path(operand).stem
        utils.bl_open_file(operand)
        utils.bl_save_as_file(utils.create_tmp_blend())

    def run(self) -> bool:
        out_dir = utils.get_build_dir() + "\\export\\models"
        utils.create_dir(out_dir)

        for w in bpy.context.window_manager.windows:
            s = w.screen
            for a in s.areas:
                if a.type == "VIEW_3D":
                    with bpy.context.temp_override(window=w, area=a):
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bpy.ops.object.select_all(action='DESELECT')

                        #todo: handle multiple exporting multiple invariant objects from one source file
                        for obj in bpy.data.objects:
                            obj.select_set(True)
                            bpy.ops.object.convert(target='MESH')
                            bpy.ops.export_scene.gltf(filepath=out_dir + "\\" + self.__base_name, export_format='GLB')
                            obj.select_set(False)

        self._cleanup()

        return True

    def _cleanup(self) -> None:
        pass
