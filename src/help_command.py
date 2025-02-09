import argparse
from .commands import commands


class HelpCommand(argparse.HelpFormatter):
    """Custom help command formatter class that includes the project's subcommands."""

    def format_help(self):
        """Adds the project's subcommands to the help message."""
        help_message = super().format_help()
        subcommands = "\n".join([f"{command}: {data['description']}"
                                 for command, data in commands.items()])
        return f"{help_message}\ncommands:\n{subcommands}"
