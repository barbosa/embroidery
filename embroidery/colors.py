import re


def sanitize_color(color):
    if not color:
        return None

    if color.startswith("#"):
        return color

    if _color_is_hex(color):
        return f"#{color}"

    return color


def _color_is_hex(color):
    regex = r"[\da-fA-F]{3}|[\da-fA-F]{6}|[\da-fA-F]{8}"
    return re.search(regex, color) is not None
