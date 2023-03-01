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

#PIPELINE
#project_dir/blender_src/models/**/<modelname>.blend
# --> project_dir/build/variants/models/**/<modelname>/<modelname>.<variant>.blend
# --> project_dir/build/binary/models/**/<modelname>/<modelname>.<variant>.glb
# --> project_dir/godot/generated/models/**/<modelname>/<modelname>.<variant>.glb

import os
from .. import core
from .gen_variants import GenVariants
from .export_models import ExportModels
from .copy_results import CopyResults
from .gen_terrain import GenTerrain

def clean() -> bool:
    core.utils.clean_build_dir()
    return True

def build(**kwargs) -> bool:
    args = {
        'variants': 5,
    }
    args.update(kwargs)
    #debug_args_update(args, kwargs)

    print("GDPG: GENERATING MODEL VARIANTS...")
    models_src = os.path.join(core.utils.get_source_dir(), "models")
    if not core.buildstep.batch_build_in_dir(GenVariants, models_src, "*.blend", **args):
        return False
    print("GDPG: GENERATING MODEL VARIANTS...DONE")

    print("GDPG: GENERATING TERRAIN VARIANTS...")
    terrain_src = os.path.join(core.utils.get_source_dir(), "terrain")
    if not core.buildstep.batch_build_in_dir(GenTerrain, terrain_src, "*.blend", **args):
        return False
    print("GDPG: GENERATING TERRAIN VARIANTS...DONE")

    print("GDPG: EXPORTING BINARY MODELS...")
    if not core.buildstep.batch_build_in_dir(ExportModels, core.utils.get_variants_dir(), "*.blend", **args):
        return False
    print("GDPG: EXPORTING BINARY MODELS...DONE")

    print("GDPG: COPYING RESULTS...")
    if not core.buildstep.batch_build_in_dir(CopyResults, core.utils.get_binary_dir(), "*.glb", **args):
        return False
    print("GDPG: COPYING RESULTS...DONE")

    return True

def clean_current() -> bool:
    print("NOT IMPLEMENTED")
    return False

def build_current() -> bool:
    print("NOT IMPLEMENTED")
    return False

def rebuild(**kwargs) -> bool:
    if not clean():
        return False
    if not build(**kwargs):
        return False

    return True

def debug_args_update(default_args: dict, kwargs: dict) -> None:
    print("cmds::debug_args(...) default_args = ")
    print(default_args)
    print("cmds::debug_args(...) kwargs = ")
    print(kwargs)
    default_args.update(kwargs)
    print("cmds::debug_args(...) updated_args= ")
    print(default_args)
