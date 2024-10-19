bl_info = {
    "name": "Pillow Auto Installer",
    "blender": (4, 1, 0),  # Update as needed for your Blender version
    "category": "System",
    "version": (1, 0),
    "author": "Your Name",
    "description": "Automatically installs Pillow module when enabled."
}

import bpy
import subprocess
import sys
import os

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

class InstallPillowOperator(bpy.types.Operator):
    """Operator to install Pillow"""
    bl_idname = "wm.install_pillow"
    bl_label = "Install Pillow"
    
    def execute(self, context):
        install_pillow()
        self.report({'INFO'}, "Pillow installed successfully!")
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(InstallPillowOperator.bl_idname)

def register():
    bpy.utils.register_class(InstallPillowOperator)
    bpy.types.TOPBAR_MT_help.append(menu_func)

def unregister():
    bpy.utils.unregister_class(InstallPillowOperator)
    bpy.types.TOPBAR_MT_help.remove(menu_func)

if __name__ == "__main__":
    register()
