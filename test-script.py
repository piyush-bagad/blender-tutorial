import bpy

# Code to get all objects in a given scene
scene = bpy.context.scene
for obj in scene.objects:
    obj.location.x += 1.0
    print(obj.name)