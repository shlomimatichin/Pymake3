"""
Provides functionality for starting process on the host operating system.

Easily done without pymake, but we want pymake to be dead simple to use, so we
include this functionality here.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import subprocess

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

    global _exit_code
    _exit_code = subprocess.call([s] + args)

    return _exit_code
