import click
import subprocess
from .builder import build_command
from .fileutils import default_output
from .geometry import TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT
from .logger import Logger


logger = Logger()


@click.command()
@click.option(
    "-f",
    "--file",
    "file",
    required=True,
    type=click.Path(exists=True),
    help="Image to apply embroidery.",
)
@click.option(
    "-c",
    "--color",
    "color",
    default="black",
    help="Background color. Defaults to black.",
)
@click.option(
    "-t",
    "--text",
    "text",
    default="",
    help="Text on top of embroidery. Defaults to None.",
)
@click.option(
    "-k", "--text-color", "text_color", default="white", help="Defaults to white."
)
@click.option(
    "-p",
    "--position",
    "position",
    type=click.Choice(
        [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT], case_sensitive=False
    ),
    default=TOP_RIGHT,
    help="Top Left, Top Right (default), Bottom Left, Bottom Right.",
)
@click.option(
    "-o",
    "--output",
    "output",
    help="Path for result image. Defaults to image name + '_embroidered'.",
)
def embroidery(**args):
    logger.log("running")

    command = build_command(**args)
    logger.log(" ".join(command))
    subprocess.run(command)

    logger.log("done")
