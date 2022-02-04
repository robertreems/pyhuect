"""
    This class handles the CLI opions and arguments.
"""

import argparse


class cliclass:
    args = ''

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Prints the argument of the message option."
        )

        parser.add_argument(
            "-v", "--verbose", action='store_true'
        )

        self.args = parser.parse_args()
