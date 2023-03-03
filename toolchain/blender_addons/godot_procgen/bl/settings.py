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

# class BuildSettings(bpy.types.PropertyGroup):

#     gen_variants : bpy.types.BoolProperty(
#         name="Generate Variants",
#         description="",
#         default = True
#         )

#     gen_terrain : bpy.types.BoolProperty(
#         name="Generate Terrain",
#         description="",
#         default = True
#         )

#     export_models : bpy.types.BoolProperty(
#         name="Export Models",
#         description="",
#         default = True
#         )

#     copy_results : bpy.types.BoolProperty(
#         name="Copy Results",
#         description="",
#         default = True
#         )

#     seed : bpy.types.IntProperty(
#         name = "Top-Level ProcGen Seed",
#         default = 0,
#         min = -50000,
#         max = 50000
#         )

class GlobalSettings(bpy.types.AddonPreferences):
    bl_idname = core.utils.get_toplevel_package()

    #todo: replace this with a project manager configurable field
    project_file: bpy.props.StringProperty(
        name = "Godot ProcGen Project File",
        subtype = "FILE_PATH",
        default= "C:\\Users\\duste\\git\\godot-procgen\\samples\\forest\\project.gdpg"
    )

    def draw(self, _context):
        layout = self.layout
        layout.label(text = "### GLOBAL SETTINGS ###")
        layout.prop(self, "project_file")

def register():
    bpy.utils.register_class(GlobalSettings)

def unregister():
    bpy.utils.unregister_class(GlobalSettings)
