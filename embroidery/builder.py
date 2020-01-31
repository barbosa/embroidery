from PIL import Image
from .colors import sanitize_color
from .fileutils import default_output
from .geometry import embroider_path


def build_ribbon_command(file, start_color, end_color, position, output):
    image_size = Image.open(file).size
    return [
        "convert",
        file,
        "-size",
        f"{image_size[0] / 2}x{image_size[1] / 2}",
        "-fill",
        f"gradient:{start_color}-{end_color if end_color else start_color}",
        "-draw",
        f"path '{embroider_path(image_size, position.upper())}'",
        output if output else default_output(file),
    ]


def build_text_command(file, position, output):
    return [
        "convert",
        # TODO
    ]
