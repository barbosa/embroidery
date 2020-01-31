from PIL import Image
from .colors import sanitize_color
from .fileutils import default_output
from .geometry import embroider_path


def build_command(**args):
    file = args.get("file")
    start_color = sanitize_color(args.get("start_color"))
    end_color = sanitize_color(args.get("end_color"))
    position = args.get("position").upper()
    output = args.get("output")

    image_size = Image.open(file).size
    return [
        "convert",
        file,
        "-size",
        f"{image_size[0] / 2}x{image_size[1] / 2}",
        # "-fill",
        # "blue",
        # "-pointsize",
        # "40",
        # "-font",
        # "Helvetica",
        # "label:BETA VERSION",
        "-fill",
        f"gradient:{start_color}-{end_color if end_color else start_color}",
        "-draw",
        f"path '{embroider_path(image_size, position)}'",
        output if output else default_output(file),
    ]
