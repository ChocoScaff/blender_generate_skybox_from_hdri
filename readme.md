
# ReadMe

This Blender Addon is designed to help you easily convert your 3D environment into a skybox for the Source Engine. It automates the process of generating the six necessary textures from different points of view, combines them into a single image for previewing, and creates the required VMT (Valve Material Type) files for each texture.

![](img/img1.png)

## Features
1. **Skybox Generation**: Capture your scene from six different perspectives (up, down, left, right, front, and back) and export the views as six `.tga` files.
2. **Stitched Skybox Preview**: Automatically combine the six textures into a single stitched image for a quick visual preview of your final skybox.
3. **VMT Generation**: Automatically generate six `.vmt` files for each skybox texture, ready for use in the Source Engine.


## Skybox Blender

The add-on will create six `.tga` files in the specified output folder, representing the six views:
   - Front (`FT`)
   - Back (`BK`)
   - Left (`LF`)
   - Right (`RT`)
   - Up (`UP`)
   - Down (`DN`)


## Skybox Stiched

1. After generating the individual textures, click **Stitch Skybox**.
2. This will generate a stitched preview image that shows all six faces of the skybox in a cross-like layout. You can use this image to quickly check how the skybox looks when assembled.


## Skybox_Generate

1. After generating the `.tga` files, click **Generate VMTs**.
2. The add-on will automatically create a `.vmt` file for each texture. These `.vmt` files contain the necessary shader and texture settings to be used in the Source Engine.

Example `.vmt` content:

```plaintext
"sky"
{
    "$basetexture" "skybox/skyboxname_FT"
    "$translucent" 1
}
```


