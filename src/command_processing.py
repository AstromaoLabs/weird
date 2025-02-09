import argparse
from .commands import commands
from .help_command import HelpCommand


def main(input_args: list):
    """Parse the CLI arguments and call the appropriate command if it exists."""
    parser = argparse.ArgumentParser(
        description="Static site generator", formatter_class=HelpCommand)
    parser.add_argument("command", type=str, help="Command to run")
    parser.add_argument("args", nargs=argparse.REMAINDER,
                        help="Arguments for the command")
    args = parser.parse_args(input_args)
    command = args.command
    if command in commands:
        commands[command]["callback"](args.args)
    else:
        print(f"Command {command} not found.")
