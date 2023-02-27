# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

from . import bl
from . import build
from . import core

import bpy
from .bl import cmds, panels, settings

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

modules = {
    cmds,
    panels,
    settings
}

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in modules:
        mod.unregister()

if __name__ == "__main__":
    register()
