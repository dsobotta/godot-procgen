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
import shutil
from . import utils
from . import build_step

class CopyResults(build_step.BuildStep):

    __src_path = ""
    __filename = ""
    __rel_path = ""

    def __init__(self, operand: str):
        self.__src_path = operand
        self.__filename = pathlib.Path(operand).name
        rel_filename = os.path.relpath(operand, utils.get_binary_dir())
        self.__rel_path = os.path.dirname(rel_filename)

    def run(self) -> bool:
        out_dir = os.path.join(utils.get_godot_generated_dir(), self.__rel_path)
        utils.create_dir(out_dir)
        out_file = os.path.join(out_dir, self.__filename)
        shutil.copyfile(self.__src_path, out_file)

        self._cleanup()

        return True

    def _cleanup(self) -> None:
        pass
