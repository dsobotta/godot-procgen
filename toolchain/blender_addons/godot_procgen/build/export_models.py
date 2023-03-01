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

class ExportModels(core.buildstep.BuildStep):

    __base_name = ""
    __rel_path = ""

    def __init__(self, operand: str, **kwargs):
        self.__base_name = pathlib.Path(operand).stem
        rel_filename = os.path.relpath(operand, core.utils.get_variants_dir())
        self.__rel_path = os.path.dirname(rel_filename)
        core.utils.bl_open_file(operand)
        #core.utils.bl_save_as_file(core.utils.create_tmp_blend())

    def run(self) -> bool:
        out_dir = os.path.join(core.utils.get_binary_dir(), self.__rel_path)
        core.utils.create_dir(out_dir)
        path = os.path.join(out_dir, self.__base_name)

        #https://blenderartists.org/t/bad-context-after-open-new-file-with-python/1398392
        for w in bpy.context.window_manager.windows:
            s = w.screen
            for a in s.areas:
                if a.type == "VIEW_3D":
                    with bpy.context.temp_override(window=w, area=a):
                        bpy.ops.export_scene.gltf(filepath=path, export_format='GLB')
                        break

        self._cleanup()

        return True

    def _cleanup(self) -> None:
        pass
