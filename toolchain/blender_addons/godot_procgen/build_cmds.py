# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

from . import utils
from .build_step import batch_build_in_dir
from .gen_variants import GenVariants
from .export_models import ExportModels

def clean() -> bool:
    utils.clean_build_dir()
    return True

def build() -> bool:
    if not batch_build_in_dir(GenVariants, utils.get_source_dir(), "*.blend"):
        return False

    #if not batch_build_in_dir(ExportModels, utils.get_models_dir(), "*.blend"):
    #    return False

    return True

def rebuild() -> bool:
    if not clean():
        return False
    if not build():
        return False

    return True
