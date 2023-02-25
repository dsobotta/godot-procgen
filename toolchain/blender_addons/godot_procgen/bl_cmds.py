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
from . import utils
from . import build_step
from .gen_variants import GenVariants
from .export_models import ExportModels

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

class BlGenVariants(bpy.types.Operator):
    bl_label = "Generate Variants"
    bl_idname = "gdpg.gen_variants"

    def execute(self, context):
        return utils.bl_result(build_step.build_open_file(GenVariants))

class BlExportModels(bpy.types.Operator):
    bl_label = "Export Models"
    bl_idname = "gdpg.export_models"

    def execute(self, context):
        return utils.bl_result(build_step.build_open_file(ExportModels))

def register():
    bpy.utils.register_class(Clean)
    bpy.utils.register_class(Build)
    bpy.utils.register_class(Rebuild)
    bpy.utils.register_class(BlGenVariants)
    bpy.utils.register_class(BlExportModels)

def unregister():
    bpy.utils.unregister_class(Clean)
    bpy.utils.unregister_class(Build)
    bpy.utils.unregister_class(Rebuild)
    bpy.utils.unregister_class(BlGenVariants)
    bpy.utils.unregister_class(BlExportModels)
