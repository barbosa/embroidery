from PIL import Image
from .colorutils import sanitize_color
from .fileutils import default_output
from .geometry import Geometry


def build_command(**args):
    file = args.get("file")
    text = args.get("text")
    position = args.get("position")
    output = args.get("output")

    bg_colors = args.get("color").split("-")
    if len(bg_colors) == 1:
        bg_colors.append(bg_colors[0])

    text_color = args.get("text_color")
    image_size = Image.open(file).size
    geometry = Geometry(image_size, position.upper())

    return [
        "convert",
        file,
        "(",
        "-size",
        geometry.size,
        "-rotate",
        geometry.rotation,
        "-background",
        "none",
        "-fill",
        sanitize_color(text_color),
        "-pointsize",
        geometry.pointsize,
        f"label:{text}",
        "-trim",
        "-gravity",
        "center",
        "-geometry",
        geometry.translation,
        "-extent",
        geometry.size,
        ")",
        "-fill",
        f"gradient:{'-'.join([sanitize_color(color) for color in bg_colors])}",
        "-draw",
        f"path '{geometry.path}'",
        "-gravity",
        geometry.gravity,
        "-composite",
        output if output else default_output(file),
    ]

