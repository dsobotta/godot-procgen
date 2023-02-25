# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy

class GDPG_PT_MainPanel(bpy.types.Panel):
    bl_idname = "GDPG_PT_MainPanel"
    bl_label = "Godot ProcGen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Godot ProcGen"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        col.label(text="All Files")
        col.operator("gdpg.clean")
        col.operator("gdpg.build")
        col.operator("gdpg.rebuild")

        col.label(text="Current File")
        col.operator("gdpg.gen_variants")
        col.operator("gdpg.export_models")

def register():
    bpy.utils.register_class(GDPG_PT_MainPanel)

def unregister():
    bpy.utils.unregister_class(GDPG_PT_MainPanel)
