# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy
from . import settings
from . import panels
#from . import gen_permutations


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
    bpy.utils.register_class(settings.GlobalSettings)
    bpy.utils.register_class(panels.GDPG_PT_MainPanel)

def unregister():
    bpy.utils.unregister_class(settings.GlobalSettings)
    bpy.utils.unregister_class(panels.GDPG_PT_MainPanel)

if __name__ == "__main__":
    register()
