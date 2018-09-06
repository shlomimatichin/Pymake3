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


def run(spec, mode="auto"):
    originalSpec = spec
    assert mode in ["auto", "exec", "split", "shell"]
    kwargs = {}
    if mode == "auto":
        if isinstance(spec, str):
            if '|' in spec or '>' in spec:
                mode = "shell"
            elif ' ' in spec:
                mode = "split"
            else:
                mode = "exec"
                spec = [spec]
        elif isinstance(spec, list):
            mode = "exec"
        else:
            raise Exception("Unable to auto determine mode for spec '%s'" % spec)

    if mode == "shell":
        kwargs['shell'] = True
    if mode == "split":
        spec = spec.split(' ')
    result = subprocess.call(spec, close_fds=True, **kwargs)
    if result != 0:
        raise Exception("Failed: run(%s)" % originalSpec)
    return True
