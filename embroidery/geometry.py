def embroider_path(image_size):
    width, height = image_size
    thickness = 0.25 * width
    tl = f"{width / 2}, 0"
    tr = f"{width / 2 + thickness}, 0"
    br = f"{width}, {height / 2 - thickness}"
    bl = f"{width}, {height / 2}"
    return f"M {tl} {tr} {br} {bl} Z"


def gradient_size(image_size):
    return (image_size[0] / 2, image_size[1] / 2)
