import bpy
import os
import configparser

# Function to render and save the cubemap face
def render_cubemap_face(output_dir, skyname, camera_rot, face_name):
    # Set the camera rotation to match the correct face
    bpy.context.scene.camera.rotation_euler = camera_rot
    
    # Set the file path for the render
    bpy.context.scene.render.filepath = os.path.join(output_dir, f"{skyname}{face_name}.tga")
    
    # Render the image
    bpy.ops.render.render(write_still=True)

def get_skybox_settings(ini_file='settings.ini'):
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__) + "/" + ini_file)
    skybox_name = config.get('Skybox', 'name')
    resolution = config.get('Skybox', 'resolution')
    return skybox_name, resolution

skyname, resolution = get_skybox_settings()

# Output directory (same folder as the .blend file or specify your own path)
output_dir = bpy.path.abspath("//")

# Create a new camera if it doesn't exist
if 'CubemapCamera' not in bpy.data.objects:
    cam_data = bpy.data.cameras.new(name='CubemapCamera')
    cam = bpy.data.objects.new('CubemapCamera', cam_data)
    bpy.context.collection.objects.link(cam)
    bpy.context.scene.camera = cam
else:
    cam = bpy.data.objects['CubemapCamera']

# Ensure the camera is at the origin
cam.location = (0.0, 0.0, 0.0)

# Set camera focal length (optional, adjust if needed)
cam.data.lens = 18

res_x, res_y = map(int, resolution.split('x'))

# Set output image settings (TGA format, 1024x1024 resolution)
bpy.context.scene.render.image_settings.file_format = 'TARGA'
bpy.context.scene.render.resolution_x = res_x
bpy.context.scene.render.resolution_y = res_y
bpy.context.scene.render.resolution_percentage = 100

# Cubemap face rotations (in radians) for each face (Back, Down, Front, Left, Right, Up)
face_rotations = {
    "BK": (1.5708, 0, 3.14159),           # Back
    "LF": (1.5708, 0, -1.5708),                 # Front
    "RT": (1.5708, 0, 1.5708),            # Left
    "FT": (1.5708, 0, 0),           # Right
    "UP": (0, 3.14159, -1.5708),           # Up
    "DN": (0, 0, 1.5708),           # Down
}

# Loop through each face and render it
for face_name, rot in face_rotations.items():
    render_cubemap_face(output_dir, skyname, rot, face_name)

print(f"Rendering completed. Images saved in: {output_dir}")
