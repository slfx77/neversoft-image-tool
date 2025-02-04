# Alpha is either 0 or 128 for some reason
argb1555_params = {
    "red_mask": 0x7C00,
    "green_mask": 0x3E0,
    "blue_mask": 0x1F,
    "alpha_mask": 0x8000,
    "red_max": 31,
    "green_max": 31,
    "blue_max": 31,
    "alpha_max": 1,
    "alpha_shift": 15,
    "red_shift": 10,
    "green_shift": 5,
}

# 565
rgb565_params = {
    "red_mask": 0xF800,
    "green_mask": 0x7E0,
    "blue_mask": 0x1F,
    "alpha_mask": 0,
    "red_max": 31,
    "green_max": 63,
    "blue_max": 31,
    "alpha_max": 0,
    "alpha_shift": 16,
    "red_shift": 11,
    "green_shift": 5,
}

# 4444
argb4444_params = {
    "red_mask": 0xF00,
    "green_mask": 0xF0,
    "blue_mask": 0xF,
    "alpha_mask": 0xF000,
    "red_max": 15,
    "green_max": 15,
    "blue_max": 15,
    "alpha_max": 15,
    "alpha_shift": 12,
    "red_shift": 8,
    "green_shift": 4,
}


def ps1_to_32bpp(color):
    r = (color) & 0x1F
    g = (color >> 5) & 0x1F
    b = (color >> 10) & 0x1F

    # Fully transparent
    if r == 31 and g == 0 and b == 31:
        return [0, 0, 0, 0]

    return [int((r / 31) * 255), int((g / 31) * 255), int((b / 31) * 255), 255]


def get_16bpp_color_params(pixel_format):
    # 0x00 = ARGB1555 (bilevel translucent alpha 0,255)
    if pixel_format & 0xF == 0:
        return argb1555_params

    # 0x01 = RGB565 (no translucent)
    if pixel_format & 0xF == 1:
        return rgb565_params

    # 0x02 = ARGB4444 (translucent alpha 0-255)
    return argb4444_params

    # 0x03 - 0x06 are other palette types supported by the PVR format, but don't seem to be used by Neversoft


def convert_16bpp_to_32bpp(params, color):
    r = (color & params["red_mask"]) >> params["red_shift"]
    g = (color & params["green_mask"]) >> params["green_shift"]
    b = color & params["blue_mask"]
    a = (color & params["alpha_mask"]) >> params["alpha_shift"]

    r = int((r / params["red_max"]) * 255)
    g = int((g / params["green_max"]) * 255)
    b = int((b / params["blue_max"]) * 255)

    a = 255 if params["alpha_max"] == 0 else int((a / params["alpha_max"]) * 255)

    return [r, g, b, a]


def convert_16_bit_texture_for_pypng(pixel_format, width, texture):
    params = get_16bpp_color_params(pixel_format)

    pixels = []
    pixel_row = []

    for i in texture:
        pixel_row += convert_16bpp_to_32bpp(params, i)
        if len(pixel_row) == width * 4:
            pixels.append(pixel_row)
            pixel_row = []

    return pixels
