# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

# Too few public methods OMEGALUL
# pylint: disable=R0903

from abc import ABC, abstractmethod
import pathlib
from . import utils

class BuildStep(ABC):

    @abstractmethod
    def __init__(self, operand: str):
        pass

    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def _cleanup(self) -> None:
        pass

def build_open_file(build_step: BuildStep) -> bool:
    orig_file = utils.bl_get_curr_file()

    step_instance = build_step(orig_file)
    result = step_instance.run()

    utils.bl_open_file(orig_file)
    return result

#todo: optimization
def batch_build_in_dir(build_step: BuildStep, root_path: str, filename_wildcard: str) -> bool:

    orig_file = utils.bl_get_curr_file()

    for file in pathlib.Path(root_path).glob("**/" + filename_wildcard):
        step_instance = build_step(str(file))
        if not step_instance.run():
            return False

    utils.bl_open_file(orig_file)
    return True
