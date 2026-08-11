import bpy
import random
# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
# Create procedural terrain (Displaced Grid)
bpy.ops.mesh.primitive_grid_db_add(size=20, x_subdivisions=64, y_subdivisions=64, location=(0, 0, -2))
terrain = bpy.context.active_object
terrain.name = "ProceduralTerrain"
# Create a Sci-Fi Drone Mesh
bpy.ops.mesh.primitive_ico_sphere_add(radius=1.5, subdivisions=2, location=(0, 0, 3))
drone = bpy.context.active_object
drone.name = "SciFiDrone"
# Add emission shader for core
mat = bpy.data.materials.new(name="CoreEmission")
mat.use_nodes = True
nodes = mat.node_tree.nodes
nodes.clear()
node_output = nodes.new(type='ShaderNodeOutputMaterial')
node_emission = nodes.new(type='ShaderNodeEmission')
node_emission.inputs['Color'].default_value = (0.0, 0.6, 1.0, 1.0)
node_emission.inputs['Strength'].default_value = 15.0
mat.node_tree.links.new(node_emission.outputs['Shader'], node_output.inputs['Surface'])
drone.data.materials.append(mat)
print("✅ Visionary3D Studio: Scene successfully generated!")
