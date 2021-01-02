import bpy
from mathutils import Matrix

class EXP_OT_explode(bpy.types.Operator):
    bl_idname = "exp.explode"
    bl_label = "Explode Operator"
    bl_description = "Explode the selected object"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        def move(obj, depth):
            print("  "*depth + obj.name)
            obj.select_set(True)
            print("  "*depth + "Before:" + str(obj.location[2]))
            obj.keyframe_insert(data_path="location", frame=0)
            bpy.ops.transform.translate(value=(0,0,0.5), orient_type='LOCAL')
            print("  "*depth + "After:" + str(obj.location[2]))
            obj.keyframe_insert(data_path="location", frame=200)
            obj.select_set(False)

        def explode(objs, depth):
            depth += 1
            for obj in objs:
                move(obj, depth)
            for obj in objs:
                if not obj.children: #check if the object has no children
                    return
                explode(obj.children, depth)

        context.scene.tool_settings.use_transform_data_origin = False
        root = context.selected_objects[0]
        print(root.name)
        root.keyframe_insert(data_path="location", frame=0)
        root.select_set(False)
        explode(root.children, 0)
        return {'FINISHED'}

classes = (
    EXP_OT_explode,
)

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