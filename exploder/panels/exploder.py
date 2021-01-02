import bpy

class EXP_PT_exploder(bpy.types.Panel):
    bl_idname = "OBJECT_PT_hello_world"
    bl_label = "Hello World"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Explode"
    bl_label = "Explode"

    def draw(self, context):
        self.layout.operator('exp.explode')

classes = [
    EXP_PT_exploder,
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()