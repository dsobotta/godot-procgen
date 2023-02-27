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
    bl_label = "Clean All"
    bl_idname = "gdpg.clean"

    def execute(self, context):
        return core.utils.bl_result(build.cmds.clean())

class Build(bpy.types.Operator):
    bl_label = "Build All"
    bl_idname = "gdpg.build"

    def execute(self, context):
        return core.utils.bl_result(build.cmds.build())

class Rebuild(bpy.types.Operator):
    bl_label = "Re-Build All"
    bl_idname = "gdpg.rebuild"

    def execute(self, context):
        return core.utils.bl_result(build.cmds.rebuild())

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

def register():
    bpy.utils.register_class(Clean)
    bpy.utils.register_class(Build)
    bpy.utils.register_class(Rebuild)
    bpy.utils.register_class(CleanCurrent)
    bpy.utils.register_class(BuildCurrent)

def unregister():
    bpy.utils.unregister_class(Clean)
    bpy.utils.unregister_class(Build)
    bpy.utils.unregister_class(Rebuild)
    bpy.utils.unregister_class(CleanCurrent)
    bpy.utils.unregister_class(BuildCurrent)
