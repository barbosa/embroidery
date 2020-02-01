from PIL import Image
from .colors import sanitize_color
from .fileutils import default_output
from .geometry import embroidery_annotation, embroidery_gravity, embroidery_path


def build_command(**args):
    file = args.get("file")
    start_color = args.get("start_color")
    end_color = args.get("end_color")
    position = args.get("position")
    output = args.get("output")

    image_size = Image.open(file).size
    return [
        "convert",
        file,
        "-size",
        f"{image_size[0] / 2}x{image_size[1] / 2}",
        "-fill",
        f"gradient:{start_color}-{end_color if end_color else start_color}",
        "-draw",
        f"path '{embroidery_path(image_size, position.upper())}'",
        "-fill",
        f"gradient:red-red",
        "-pointsize",
        "22",
        "-gravity",
        embroidery_gravity(position.upper()),
        "-annotate",
        embroidery_annotation(position.upper()),
        "BETA",
        output if output else default_output(file),
    ]

