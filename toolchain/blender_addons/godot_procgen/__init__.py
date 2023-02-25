# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy
from . import bl_cmds
from . import bl_panels
from . import bl_settings

#notes
#python-defined geo nodes -  https://devtalk.blender.org/t/extra-nodes-for-geometrynodes/20942/2

bl_info = {
    "category": "Godot",
    "name": "Procedural Generation",
    "description": "Procedural generation of assets, ready for use in Godot",
    "location": "View3D > Godot ProcGen",
    "author": "Dusten Sobotta",
    "blender": (3,4,1),
    "version": (0,0,1)
}

def register():
    bl_cmds.register()
    bl_panels.register()
    bl_settings.register()

def unregister():
    bl_cmds.unregister()
    bl_panels.unregister()
    bl_settings.unregister()

if __name__ == "__main__":
    register()
