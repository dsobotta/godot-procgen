# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import os
from . import utils
from .build_step import batch_build_in_dir
from .gen_variants import GenVariants
from .export_models import ExportModels

def clean() -> bool:
    utils.clean_build_dir()
    return True

def build() -> bool:

    print("GDPG: GENERATING MODEL VARIANTS...")
    path = os.path.join(utils.get_source_dir(), "models")
    if not batch_build_in_dir(GenVariants, path, "*.blend"):
        return False
    print("GDPG: GENERATING MODEL VARIANTS...DONE")

    print("GDPG: EXPORTING MODELS...")
    path = os.path.join(utils.get_build_dir(), "assets", "models")
    if not batch_build_in_dir(ExportModels, path, "*.blend"):
        return False
    print("GDPG: EXPORTING MODELS...DONE")

    return True

def rebuild() -> bool:
    if not clean():
        return False
    if not build():
        return False

    return True
