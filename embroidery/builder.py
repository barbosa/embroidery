from PIL import Image
from .colorutils import sanitize_color
from .fileutils import default_output
from .geometry import embroidery_annotation, embroidery_gravity, embroidery_path


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
    return [
        "convert",
        file,
        "-size",
        f"{image_size[0] / 2}x{image_size[1] / 2}",
        "-fill",
        f"gradient:{'-'.join([sanitize_color(color) for color in bg_colors])}",
        "-draw",
        f"path '{embroidery_path(image_size, position.upper())}'",
        "-fill",
        f"gradient:{'-'.join([sanitize_color(color) for color in text_colors])}",
        "-pointsize",
        "22",
        "-gravity",
        embroidery_gravity(position.upper()),
        "-annotate",
        embroidery_annotation(position.upper()),
        text,
        output if output else default_output(file),
    ]

