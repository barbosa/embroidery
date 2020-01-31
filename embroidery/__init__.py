import click
import subprocess
from PIL import Image
from .fileutils import default_output
from .geometry import embroider_path, gradient_size


@click.command()
@click.option("-f", "--file", "file", required=True, type=click.Path(exists=True))
@click.option("-s", "--start-color", "start_color", default="white")
@click.option("-e", "--end-color", "end_color")
@click.option("-o", "--output", "output")
def embroider(file, start_color, end_color, output):
    print("running")
    image_size = Image.open(file).size
    subprocess.run(
        [
            "convert",
            file,
            "-size",
            f"{gradient_size(image_size)[0]}x{gradient_size(image_size)[1]}",
            "-fill",
            f"gradient:{start_color}-{end_color if end_color else start_color}",
            "-draw",
            f"path '{embroider_path(image_size)}'",
            output if output else default_output(file),
        ]
    )
    print("done")
