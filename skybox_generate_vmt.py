import os

# Function to generate a VMT file for each cubemap face
def generate_vmt(skybox_name, output_dir):
    # VMT template with escaped curly braces
    vmt_template = '''"UnlitGeneric"
{{
    "$basetexture" "skybox/{texture_name}"
    "$translucent" 1
}}'''
    
    # Define the six skybox faces
    faces = ['BK', 'DN', 'FT', 'LF', 'RT', 'UP']
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each face and create the corresponding VMT file
    for face in faces:
        # Create the file path and name
        file_name = f"{skybox_name}{face}.vmt"
        file_path = os.path.join(output_dir, file_name)
        
        # Create the VMT content by replacing the placeholder in the template
        vmt_content = vmt_template.format(texture_name=f"{skybox_name}{face}")
        
        # Write the VMT content to the file
        with open(file_path, 'w') as f:
            f.write(vmt_content)
        
        print(f"Generated {file_name} in {output_dir}")

# Input skybox name and output directory
# Set your skybox name here
blend_file_path = bpy.data.filepath
# Extract the file name without the extension
blend_file_name = os.path.splitext(os.path.basename(blend_file_path))[0]

skybox_name = blend_file_name  # Change this to your desired skybox name
output_dir = bpy.path.abspath("//") + "./skybox"  # Change this to your desired output directory

# Call the function to generate VMT files
generate_vmt(skybox_name, output_dir)
