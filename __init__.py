bl_info = {
    "name": "Blender_generate_skybox",
    "blender": (4, 1, 0),  # Adjust this depending on your Blender version
    "category": "Object",
    "version": (0, 1),
    "author": "ChocoScaff",
    "description": "Convert environment to skybox"
}

import bpy
import os
import configparser
import subprocess
import sys

# Function to get the add-on directory
def get_addon_directory():
    return os.path.dirname(__file__)

# Function to write settings to 'settings.ini'
def write_settings(ini_file, skybox_name, resolution):
    config = configparser.ConfigParser()

    # Create a [Skybox] section in the INI file
    config['Skybox'] = {
        'name': skybox_name,
        'resolution': resolution
    }

    # Write to settings.ini file
    with open(ini_file, 'w') as configfile:
        config.write(configfile)
    print(f"Settings written to {ini_file}")

# Function to initialize settings if they don't exist
def initialize_settings(context):
    addon_dir = get_addon_directory()
    ini_file = os.path.join(addon_dir, 'settings.ini')

    # Try to read the settings.ini file if it exists
    config = configparser.ConfigParser()

    # If the file doesn't exist, write it with default values
    if not os.path.exists(ini_file):
        print(f"Settings file not found, creating new {ini_file}")
        skybox_name = context.scene.skybox_name
        resolution = context.scene.texture_resolution
        write_settings(ini_file, skybox_name, resolution)
        return

    # Read the file if it exists, and check for the Skybox section
    config.read(ini_file)
    if 'Skybox' not in config.sections():
        print(f"Skybox section not found in {ini_file}, creating new section")
        skybox_name = context.scene.skybox_name
        resolution = context.scene.texture_resolution
        write_settings(ini_file, skybox_name, resolution)
    else:
        print(f"Skybox section found in {ini_file}")

# New operator to save settings manually
class SaveSettingsOperator(bpy.types.Operator):
    """Save Skybox Settings to settings.ini"""
    bl_idname = "wm.save_skybox_settings"
    bl_label = "Save Settings"

    def execute(self, context):
        addon_dir = get_addon_directory()
        ini_file = os.path.join(addon_dir, 'settings.ini')

        # Get the current values of skybox_name and resolution
        skybox_name = context.scene.skybox_name
        resolution = context.scene.texture_resolution

        # Save these values to the settings.ini file
        write_settings(ini_file, skybox_name, resolution)

        self.report({'INFO'}, f"Settings saved: {skybox_name}, {resolution}")
        return {'FINISHED'}

# Operators for each button
class Skybox_Blender(bpy.types.Operator):
    """Execute Python File 1"""
    bl_idname = "wm.execute_file_1"
    bl_label = "Skybox_Blender"

    def execute(self, context):
        addon_dir = get_addon_directory()
        filepath = addon_dir + "/skybox_blender.py"  # Update with your file path
        initialize_settings(context)  # Write settings before executing the file
        exec(compile(open(filepath).read(), filepath, 'exec'))
        return {'FINISHED'}

class Skybox_Stiched(bpy.types.Operator):
    """Execute Python File 2"""
    bl_idname = "wm.execute_file_2"
    bl_label = "Skybox_Stiched"

    def execute(self, context):
        addon_dir = get_addon_directory()
        filepath = addon_dir + "/skybox_stiched.py"  # Update with your file path
        initialize_settings(context)  # Write settings before executing the file
        exec(compile(open(filepath).read(), filepath, 'exec'))
        return {'FINISHED'}

class Skybox_Generate_VMT(bpy.types.Operator):
    """Execute Python File 3"""
    bl_idname = "wm.execute_file_3"
    bl_label = "Skybox_Generate_VMT"

    def execute(self, context):
        addon_dir = get_addon_directory()
        filepath = addon_dir + "/skybox_generate_vmt.py"  # Update with your file path
        initialize_settings(context)  # Write settings before executing the file
        exec(compile(open(filepath).read(), filepath, 'exec'))
        return {'FINISHED'}

# Create a Panel with options for skybox name and resolution
class ExecutePythonFilesPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Execute Python Files"
    bl_idname = "OBJECT_PT_execute_python_files"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Skybox'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Dropdown for texture resolution
        layout.prop(scene, "texture_resolution", text="Texture Resolution")
        
        # Input for skybox name
        layout.prop(scene, "skybox_name", text="Skybox Name")

        # Create buttons for each operator
        layout.operator("wm.execute_file_1", text="Skybox_Blender")
        layout.operator("wm.execute_file_2", text="Skybox_Stiched")
        layout.operator("wm.execute_file_3", text="Skybox_Generate_VMT")

        # Add Save Settings button
        layout.operator("wm.save_skybox_settings", text="Save Settings")

def install_pillow():
    """Function to check and install Pillow if it's not already installed."""
    try:
        import PIL  # Try importing Pillow to see if it's already installed
        print("Pillow is already installed.")
    except ImportError:
        # Pillow not found, install it using Blender's Python environment
        try:
            python_executable = sys.executable
            print(f"Installing Pillow using: {python_executable}")
            subprocess.check_call([python_executable, "-m", "ensurepip", "--upgrade"])
            subprocess.check_call([python_executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([python_executable, "-m", "pip", "install", "Pillow"])
            print("Pillow has been installed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Pillow: {e}")

# Register and Unregister the classes
def register():
    bpy.utils.register_class(SaveSettingsOperator)
    bpy.utils.register_class(Skybox_Blender)
    bpy.utils.register_class(Skybox_Stiched)
    bpy.utils.register_class(Skybox_Generate_VMT)
    bpy.utils.register_class(ExecutePythonFilesPanel)
    
    # Add properties to Scene
    bpy.types.Scene.texture_resolution = bpy.props.EnumProperty(
        name="Texture Resolution",
        description="Select texture resolution",
        items=[
            ("1024x1024", "1024x1024", "Low resolution"),
            ("2048x2048", "2048x2048", "Medium resolution"),
            ("4096x4096", "4096x4096", "High resolution")
        ],
        default="1024x1024"
    )

    bpy.types.Scene.skybox_name = bpy.props.StringProperty(
        name="Skybox Name",
        description="Name of the skybox",
        default="default_skybox"
    )
    install_pillow()    

def unregister():
    bpy.utils.unregister_class(Skybox_Blender)
    bpy.utils.unregister_class(Skybox_Stiched)
    bpy.utils.unregister_class(Skybox_Generate_VMT)
    bpy.utils.unregister_class(SaveSettingsOperator)
    bpy.utils.unregister_class(ExecutePythonFilesPanel)
    
    # Remove properties from Scene
    del bpy.types.Scene.texture_resolution
    del bpy.types.Scene.skybox_name

if __name__ == "__main__":
    register()
