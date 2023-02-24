import bpy

bl_info = {
    "name": "Godot ProcGen",
    "description": "Procedural generation of assets, ready for use in Godot",
    "author": "Dusten Sobotta",
    "blender": (3,4,1),
    "version": (0,0,1),
    "category": "Godot ProcGen",
    "location:": "View3D > Godot ProcGen",
}

class GODOTPROCGEN_PT_Panel(bpy.types.Panel):
    bl_idname = "GODOTPROCGEN_PT_Panel"
    bl_label = "Godot ProcGen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Godot ProcGen"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="YEP")

def register():
    bpy.utils.register_class(GODOTPROCGEN_PT_Panel)

def unregister():
    bpy.utils.unregister_class(GODOTPROCGEN_PT_Panel)

if __name__ == "__main__":
    register()
