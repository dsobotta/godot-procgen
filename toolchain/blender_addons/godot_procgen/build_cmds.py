# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

from . import utils
from . import gen_variants

def clean() -> bool:
    utils.clean_build_dir()
    return True

def build() -> bool:
    if not gen_variants.run():
        return False

    return True

def rebuild() -> bool:
    if not clean():
        return False
    if not build():
        return False

    return True
