import click
import subprocess
from .builder import build_command
from .fileutils import default_output
from .geometry import TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT
from .logger import Logger


logger = Logger()


@click.command()
@click.option("-f", "--file", "file", required=True, type=click.Path(exists=True))
@click.option("-s", "--start-color", "start_color", default="black")
@click.option("-e", "--end-color", "end_color")
@click.option(
    "-p",
    "--position",
    "position",
    type=click.Choice(
        [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT], case_sensitive=False
    ),
    default=TOP_RIGHT,
)
@click.option("-o", "--output", "output")
def embroidery(**args):
    logger.log("running")

    command = build_command(**args)
    logger.log(" ".join(command))
    subprocess.run(command)

    logger.log("done")
