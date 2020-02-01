TOP_LEFT = "TL"
TOP_RIGHT = "TR"
BOTTOM_LEFT = "BL"
BOTTOM_RIGHT = "BR"


class InvalidEmbroideryPosition(Exception):
    pass


def embroidery_path(image_size, position):
    width, height = image_size
    thickness = 0.25 * width

    if position == TOP_LEFT:
        p1 = f"{width / 2 - thickness},0"
        p2 = f"{width / 2},0"
        p3 = f"0,{height / 2}"
        p4 = f"0,{height / 2 - thickness}"
    elif position == TOP_RIGHT:
        p1 = f"{width / 2},0"
        p2 = f"{width / 2 + thickness},0"
        p3 = f"{width},{height / 2 - thickness}"
        p4 = f"{width},{height / 2}"
    elif position == BOTTOM_LEFT:
        p1 = f"0,{height / 2}"
        p2 = f"{width / 2},{height}"
        p3 = f"{width / 2 - thickness},{height}"
        p4 = f"0,{height / 2 + thickness}"
    elif position == BOTTOM_RIGHT:
        p1 = f"{width / 2},{height}"
        p2 = f"{width},{height / 2}"
        p3 = f"{width},{height / 2 + thickness}"
        p4 = f"{width / 2 + thickness},{height}"
    else:
        raise InvalidEmbroideryPosition()

    return f"M {p1} {p2} {p3} {p4} Z"
