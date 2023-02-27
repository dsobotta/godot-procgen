# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

#PIPELINE
#project_dir/blender_src/models/**/<modelname>.blend
# --> project_dir/build/variants/models/**/<modelname>/<modelname>.<variant>.blend
# --> project_dir/build/binary/models/**/<modelname>/<modelname>.<variant>.glb
# --> project_dir/godot/generated/models/**/<modelname>/<modelname>.<variant>.glb

import os
from . import utils
from .build_step import batch_build_in_dir
from .gen_variants import GenVariants
from .export_models import ExportModels
from .copy_results import CopyResults

def clean() -> bool:
    utils.clean_build_dir()
    return True

def build() -> bool:

    print("GDPG: GENERATING MODEL VARIANTS...")
    models_src = os.path.join(utils.get_source_dir(), "models")
    if not batch_build_in_dir(GenVariants, models_src, "*.blend"):
        return False
    print("GDPG: GENERATING MODEL VARIANTS...DONE")

    print("GDPG: EXPORTING BINARY MODELS...")
    if not batch_build_in_dir(ExportModels, utils.get_variants_dir(), "*.blend"):
        return False
    print("GDPG: EXPORTING BINARY MODELS...DONE")

    print("GDPG: COPYING RESULTS...")
    if not batch_build_in_dir(CopyResults, utils.get_binary_dir(), "*.glb"):
        return False
    print("GDPG: COPYING RESULTS...DONE")

    return True

def clean_current() -> bool:
    print("NOT IMPLEMENTED")
    return False

def build_current() -> bool:
    print("NOT IMPLEMENTED")
    return False

def rebuild() -> bool:
    if not clean():
        return False
    if not build():
        return False

    return True
