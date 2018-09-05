"""
Provides functionality for starting process on the host operating system.
    Easily done without pymake3, but we want pymake3 to be dead simple to use,
so we include this functionality here.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import subprocess

from pymake3.cli import main

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

    result = subprocess.call([s] + args)
    main.exit_code = result
    return result
