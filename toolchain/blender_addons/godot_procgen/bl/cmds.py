# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy
from .. import core
from .. import build

class Clean(bpy.types.Operator):
    bl_label = "Clean"
    bl_idname = "gdpg.clean"

    def execute(self, context):
        return core.utils.bl_result(build.cmds.clean())

class Build(bpy.types.Operator):
    bl_label = "Build"
    bl_idname = "gdpg.build"

    gen_variants    : bpy.props.BoolProperty(name="Generate Variants")
    gen_terrain     : bpy.props.BoolProperty(name="Generate Terrain")
    export_models   : bpy.props.BoolProperty(name="Export Models")
    copy_results    : bpy.props.BoolProperty(name="Copy Results")

    def execute(self, context):
        args = {
            'gen_variants'  : True,
            'variants'      : 5,
            'gen_terrain'   : True,
            'export_models' : True,
            'copy_results'  : True
        }
        return core.utils.bl_result(build.cmds.build(**args))

class Rebuild(bpy.types.Operator):
    bl_label = "Re-Build"
    bl_idname = "gdpg.rebuild"

    gen_variants    : bpy.props.BoolProperty(name="Generate Variants")
    gen_terrain     : bpy.props.BoolProperty(name="Generate Terrain")
    export_models   : bpy.props.BoolProperty(name="Export Models")
    copy_results    : bpy.props.BoolProperty(name="Copy Results")

    def execute(self, context):
        args = {
            'gen_variants'  : True,
            'variants'      : 5,
            'gen_terrain'   : True,
            'export_models' : True,
            'copy_results'  : True
        }
        return core.utils.bl_result(build.cmds.rebuild(**args))

class CleanCurrent(bpy.types.Operator):
    bl_label = "Clean Current File"
    bl_idname = "gdpg.clean_current"

    def execute(self, context):
        return core.utils.bl_result(build.cmds.clean_current())

class BuildCurrent(bpy.types.Operator):
    bl_label = "Build Current File"
    bl_idname = "gdpg.build_current"

    def execute(self, context):
        return core.utils.bl_result(build.cmds.build_current())

_operators = [
    Clean,
    Build,
    Rebuild,
    #CleanCurrent,
    #BuildCurrent
]

def register():
    for op in _operators:
        bpy.utils.register_class(op)

def unregister():
    for op in _operators:
        bpy.utils.unregister_class(op)
