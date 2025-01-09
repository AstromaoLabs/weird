import argparse


class Build:
    """Class to build the site.

    NOT IMPLEMENTED
    """
    @staticmethod
    def build(input_path: str, output_path: str, config_path: str) -> None:
        """Build the site."""
        print(f"Building site from {input_path} to {
              output_path} using {config_path}")

    @staticmethod
    def run(input_args: list) -> None:
        """Parse the build command arguments and call the build method."""
        parser = argparse.ArgumentParser(
            prog="build", description="Build the site.")
        parser.add_argument("input_path", type=str, help="Path to input files")
        parser.add_argument("output_path", type=str,
                            help="Path to output files")
        parser.add_argument("config_path", type=str,
                            help="Path to config file")
        args = parser.parse_args(input_args)
        Build.build(args.input_path, args.output_path, args.config_path)
