from PIL import Image

# Define the filenames for the six skybox textures
# Set your skybox name here
blend_file_path = bpy.data.filepath
# Extract the file name without the extension
blend_file_name = os.path.splitext(os.path.basename(blend_file_path))[0]
skyname = blend_file_name

file_names = {
    "Front": f"{skyname}FT.tga",
    "Left": f"{skyname}LF.tga",
    "Back": f"{skyname}BK.tga",
    "Right": f"{skyname}RT.tga",
    "Up": f"{skyname}UP.tga",
    "Down": f"{skyname}DN.tga"
}

path = bpy.path.abspath("//")
# Load the six images
front = Image.open(path + file_names["Front"])
left = Image.open(path + file_names["Left"])
back = Image.open(path + file_names["Back"])
right = Image.open(path + file_names["Right"])
up = Image.open(path + file_names["Up"])
down = Image.open(path + file_names["Down"])

# Get the size of one image (assuming all images have the same size)
width, height = front.size

# Create a new blank image with the layout of 4x3 grid (4 wide, 3 tall)
# Width: 4 * width, Height: 3 * height
output_image = Image.new('RGB', (4 * width, 3 * height), color=(128, 128, 128))

# Paste the images into the appropriate locations in the grid
# Place them in this layout:
#   [  X,  X,  Up,  X ]
#   [Front, Left, Back, Right]
#   [  X,  X, Down,  X ]

output_image.paste(up, (2 * width, 0 * height))     # Up
output_image.paste(front, (0 * width, 1 * height))  # Front
output_image.paste(left, (1 * width, 1 * height))   # Left
output_image.paste(back, (2 * width, 1 * height))   # Back
output_image.paste(right, (3 * width, 1 * height))  # Right
output_image.paste(down, (2 * width, 2 * height))   # Down

# Save the final composite image as a .TGA file
output_image.save(f"{path}/{skyname}_stitched.tga")
print(f"Stitched image saved as {skyname}stitched.tga")
