# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

from . import utils

def run() -> bool:
    _tmp_file = utils.create_tmp_blend()

    return True
