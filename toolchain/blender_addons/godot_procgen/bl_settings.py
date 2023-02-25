# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy

class GlobalSettings(bpy.types.AddonPreferences):
    bl_idname = __package__

    source_dir: bpy.props.StringProperty(
        name = "Source Assets",
        subtype = "FILE_PATH",
        default= "C:\\Users\\duste\\git\\godot-procgen\\blender\\"
    )

    build_dir: bpy.props.StringProperty(
        name = "Build Path",
        subtype = "FILE_PATH",
        default= "C:\\Users\\duste\\git\\godot-procgen\\build\\"
    )

    def draw(self, _context):
        layout = self.layout
        layout.label(text = "### GLOBAL SETTINGS ###")
        layout.prop(self, "source_dir")
        layout.prop(self, "build_dir")

def register():
    bpy.utils.register_class(GlobalSettings)

def unregister():
    bpy.utils.unregister_class(GlobalSettings)
