import bpy
from mathutils import Matrix

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

bpy.context.scene.tool_settings.use_transform_data_origin = False
root = bpy.context.selected_objects[0]
print(root.name)
root.keyframe_insert(data_path="location", frame=0)
root.select_set(False)
explode(root.children, 0)