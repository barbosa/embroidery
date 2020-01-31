import click
import subprocess
from .builder import build_ribbon_command, build_text_command
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
def embroidery(file, start_color, end_color, position, output):
    logger.log("running")

    ribbon_command = build_ribbon_command(
        file, start_color, end_color, position, output
    )
    logger.log(" ".join(ribbon_command))
    subprocess.run(ribbon_command)

    # text_command = build_text_command(output, position, output)
    # logger.log(" ".join(text_command))
    # subprocess.run(text_command)

    logger.log("done")
