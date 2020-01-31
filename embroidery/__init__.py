import click
import subprocess
from .builder import build_command
from .logger import Logger


logger = Logger()


@click.command()
@click.option("-f", "--file", "file", required=True, type=click.Path(exists=True))
@click.option("-s", "--start-color", "start_color", default="white")
@click.option("-e", "--end-color", "end_color")
@click.option(
    "-p", "--position", "position",
)
@click.option("-o", "--output", "output")
def embroider(**args):
    logger.log("running")

    command = build_command(**args)
    logger.log(" ".join(command))

    subprocess.run(command)

    logger.log("done")
