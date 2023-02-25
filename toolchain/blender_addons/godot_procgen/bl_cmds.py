# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy
from . import build_cmds
from . import gen_variants
from . import utils


class Clean(bpy.types.Operator):
    bl_label = "Clean All"
    bl_idname = "gdpg.clean"

    def execute(self, context):
        return utils.bl_result(build_cmds.clean())

class Build(bpy.types.Operator):
    bl_label = "Build All"
    bl_idname = "gdpg.build"

    def execute(self, context):
        return utils.bl_result(build_cmds.build())

class Rebuild(bpy.types.Operator):
    bl_label = "Re-Build All"
    bl_idname = "gdpg.rebuild"

    def execute(self, context):
        return utils.bl_result(build_cmds.rebuild())


class GenVariants(bpy.types.Operator):
    bl_label = "Generate Variants"
    bl_idname = "gdpg.gen_variants"

    def execute(self, context):
        return utils.bl_result(gen_variants.run())

def register():
    bpy.utils.register_class(Clean)
    bpy.utils.register_class(Build)
    bpy.utils.register_class(Rebuild)
    bpy.utils.register_class(GenVariants)

def unregister():
    bpy.utils.unregister_class(Clean)
    bpy.utils.unregister_class(Build)
    bpy.utils.unregister_class(Rebuild)
    bpy.utils.unregister_class(GenVariants)
