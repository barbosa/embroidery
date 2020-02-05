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

    text_colors = args.get("text_color").split("-")
    if len(text_colors) == 1:
        text_colors.append(text_colors[0])

    image_size = Image.open(file).size
    geometry = Geometry(image_size, position.upper())

    return [
        "convert",
        file,
        "(",
        "-size",
        f"{image_size[0] / 2}x{image_size[1] / 2}",
        # "-rotate",
        # "45",
        "-background",
        "#ff000033",
        "-pointsize",
        str(geometry.pointsize),
        f"label:{text}",
        "-trim",
        "-gravity",
        "center",
        # "-geometry",
        # f"-{geometry.thickness / 2}-{geometry.thickness / 2}",
        "-extent",
        f"{image_size[0] / 2}x{image_size[1] / 2}",
        ")",
        "-fill",
        f"gradient:{'-'.join([sanitize_color(color) for color in bg_colors])}",
        "-draw",
        f"path '{geometry.path}'",
        "-gravity",
        "northeast",
        "-composite",
        output if output else default_output(file),
    ]

