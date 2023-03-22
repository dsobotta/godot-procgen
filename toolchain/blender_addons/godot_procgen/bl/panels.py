# Missing class docstring
# pylint: disable=C0103

# Missing module docstring
# pylint: disable=C0114

# Missing class docstring
# pylint: disable=C0115

# Missing function or method docstring
# pylint: disable=C0116

import bpy

class GDPG_PT_BuildOptions(bpy.types.Panel):
    bl_parent_id = "GDPG_PT_MainPanel"
    bl_idname = "GDPG_PT_BuildOptions"
    bl_label = "Build Options"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.label(text="test123")

class GDPG_PT_Build(bpy.types.Panel):
    bl_parent_id = "GDPG_PT_MainPanel"
    bl_idname = "GDPG_PT_Build"
    bl_label = "Build"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_options = {'DEFAULT_CLOSED,'HIDE_HEADER', 'INSTANCED', 'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        layout = self.layout
 
        layout.operator("gdpg.clean")
        op = layout.operator("gdpg.build")
        op.gen_variants    = True
        op.gen_terrain     = True
        op.export_models   = True
        op.copy_results    = True
        layout.operator("gdpg.rebuild")

class GDPG_PT_MainPanel(bpy.types.Panel):
    bl_idname = "GDPG_PT_MainPanel"
    bl_label = "Godot ProcGen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Godot ProcGen"
    bl_context = "objectmode"

    def draw(self, context):
        pass
        #layout = self.layout
        #col = layout.column()

        #sub = col.column()
        #sub.label(text="All Files")

        #sub = col.column()
        #sub.label(text="Current File")
        #sub.operator("gdpg.clean_current")
        #sub.operator("gdpg.build_current")

_panels = [
    GDPG_PT_MainPanel,
    GDPG_PT_BuildOptions,
    GDPG_PT_Build
]

def register():
    for panel in _panels:
        bpy.utils.register_class(panel)

def unregister():
    for panel in _panels:
        bpy.utils.unregister_class(panel)
