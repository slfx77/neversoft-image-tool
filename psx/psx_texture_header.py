class PSXTextureHeader:
    # An unknown value, possibly a header or some format-specific information.
    unk = 0

    # The size of the color palette, which determines the bit depth of the texture.
    pal_size = 0

    # A hash value associated with the texture.
    hash = 0

    # The index of the texture in the file.
    index = 0

    # The width of the texture in pixels.
    width = 0

    # The height of the texture in pixels.
    height = 0

    # The pixel_format for PVR textures.
    pixel_format = 0

    # The size of the texture data in bytes for PVR textures.
    size = 0

    ## Extra data (not part of the header but used for conversion) ##

    # The offset in the file where the texture's header is located.
    offset = 0

    # The offset in the file where the texture's data is located.
    texture_offset = 0
