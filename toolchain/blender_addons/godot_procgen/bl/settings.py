# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

from .. import core

import bpy

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
