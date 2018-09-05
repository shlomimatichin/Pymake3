"""
Parses command-line options for pymake3.
"""
#---------------------------------------
# IMPORTS
#---------------------------------------

import ast
import os
import sys

from pymake3      import report
from pymake3.cli  import info
from pymake3.core import makeconf

#---------------------------------------
# GLOBALS
#---------------------------------------

# Make configuration specified on command-line.
conf = None

# Indicates whether colors should be disabled when printing to stdout.
disable_color = False

# Whether warnings should be disabled.
disable_warnings = False

# All known options and their associated functions.
options = {}

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def option(name):
    """
    Registers a function as a handler for the specified command-line option.

    :param name: The command line option that the function handles.
    """
    def reg_option(func):
        options[name] = func
        return func

    return reg_option

@option('--conf')
def option_conf(value):
    """
    Allows the user to specify a make configuration on the command line.

    :param value: Option value string to parse into make configuration.
    """
    global conf
    conf = makeconf.from_dict(ast.literal_eval(value))

@option('--help')
def option_help(value):
    """
    Prints usage text.

    :param value: Not used.
    """
    info.print_usage()
    sys.exit(0)

@option('--no-color')
def option_no_color(value):
    """
    Disables the use of color when printing text.

    :param value: Not used.
    """
    global disable_color
    disable_color = True

@option('--no-warn')
def option_no_warn(value):
    """
    Disables warnings.

    :param value: Not used.
    """
    global disable_warnings
    disable_warnings = True

@option('--targets')
def option_targets(value):
    """
    Prints information about known targets.

    :param value: Not used.
    """
    info.print_targets()
    sys.exit(0)

@option('--version')
def option_version(value):
    """
    Prints the pymake3 version number.

    :param value: Not used.
    """
    from . import __version__
    println("pymake3 v{}", __version__)

def parse(opts):
    """
    Parses and handles the specified option strings.

    :param opts: Array of option strings to parse and handled.
    """
    for opt in opts:
        val = None

        # Split into <opt>=<val> if possible.
        if opt.find('=') > 0:
            s   = opt.split('=', 1)
            opt = s[0].strip()
            val = s[1].strip()

        if not opt in options:
            report.warn("unknown option: '{}'", opt)
            continue

        options[opt](val)
