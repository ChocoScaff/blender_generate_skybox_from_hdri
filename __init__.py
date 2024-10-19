bl_info = {
    "name": "Execute Python Files",
    "blender": (4, 1, 0),  # Adjust this depending on your Blender version
    "category": "Object",
    "version": (0, 1),
    "author": "ChocoScaff",
    "description": "Convert environnement to skybox"
}

import bpy
import os

# Function to execute a Python file
def execute_python_file(filepath):
    if os.path.exists(filepath):
        exec(compile(open(filepath).read(), filepath, 'exec'))
        print(f"Executed: {filepath}")
    else:
        print(f"File not found: {filepath}")

def get_addon_directory():
    return os.path.dirname(__file__)
    
# Operators for each button
class Skybox_Blender(bpy.types.Operator):
    """Execute Python File 1"""
    bl_idname = "wm.execute_file_1"
    bl_label = "Skybox_Blender"
    
    def execute(self, context):
        addon_dir = get_addon_directory()
        filepath = addon_dir + "/skybox_blender.py"  # Update with your file path
        execute_python_file(filepath)
        return {'FINISHED'}

class Skybox_Stiched(bpy.types.Operator):
    """Execute Python File 2"""
    bl_idname = "wm.execute_file_2"
    bl_label = "Skybox_Stiched"
    
    def execute(self, context):
        addon_dir = get_addon_directory()
        filepath = addon_dir + "/skybox_stiched.py"  # Update with your file path
        execute_python_file(filepath)
        return {'FINISHED'}

class Skybox_Generate_VMT(bpy.types.Operator):
    """Execute Python File 3"""
    bl_idname = "wm.execute_file_3"
    bl_label = "Skybox_Generate_VMT"
    
    def execute(self, context):
        addon_dir = get_addon_directory()
        filepath = addon_dir + "/skybox_generate_vmt.py"  # Update with your file path
        execute_python_file(filepath)
        return {'FINISHED'}

# Create a Panel with 3 buttons
class ExecutePythonFilesPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Execute Python Files"
    bl_idname = "OBJECT_PT_execute_python_files"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Skybox'

    def draw(self, context):
        layout = self.layout
        
        # Create buttons for each operator
        layout.operator("wm.execute_file_1", text="Skybox_Blender")
        layout.operator("wm.execute_file_2", text="Skybox_Stiched")
        layout.operator("wm.execute_file_3", text="Skybox_Generate_VMT")

def install_pillow():
    """ Function to check and install Pillow if it's not already installed. """
    try:
        import PIL  # Try importing Pillow to see if it's already installed
        print("Pillow is already installed.")
    except ImportError:
        # Pillow not found, install it using Blender's Python environment
        python_executable = sys.executable
        print(f"Installing Pillow using: {python_executable}")
        subprocess.call([python_executable, "-m", "ensurepip", "--upgrade"])
        subprocess.call([python_executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.call([python_executable, "-m", "pip", "install", "Pillow"])
        print("Pillow has been installed.")

# Register and Unregister the classes
def register():
    bpy.utils.register_class(Skybox_Blender)
    bpy.utils.register_class(Skybox_Stiched)
    bpy.utils.register_class(Skybox_Generate_VMT)
    bpy.utils.register_class(ExecutePythonFilesPanel)

def unregister():
    bpy.utils.unregister_class(Skybox_Blender)
    bpy.utils.unregister_class(Skybox_Stiched)
    bpy.utils.unregister_class(Skybox_Generate_VMT)
    bpy.utils.unregister_class(ExecutePythonFilesPanel)

if __name__ == "__main__":
    install_pillow()
    register()
