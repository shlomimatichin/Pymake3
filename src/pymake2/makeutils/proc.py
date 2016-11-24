"""
Provides functionality for starting process on the host operating system.

Easily done without pymake2, but we want pymake2 to be dead simple to use, so we
include this functionality here.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import subprocess

from pymake2 import cli

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def run_program(s, args=None):
    """
    Runs the specified program with the specified arguments.

    :param s:    Name of the program to run.
    :param args: Program arguments.

    :return: Exit code returned by the executed program.
    """

    if not args:
        args = []

    r = subprocess.call([s] + args)

    cli.exit_code = r

    return r
