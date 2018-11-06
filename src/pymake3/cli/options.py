import ast
import os
import sys

from pymake3      import report
from pymake3.cli  import info
from pymake3.core import makeconf

# Make configuration specified on command-line.
conf = None

# Indicates whether colors should be disabled when printing to stdout.
disable_color = False

# Whether warnings should be disabled.
disable_warnings = False


def option_conf(value):
    global conf
    conf = makeconf.from_dict(ast.literal_eval(value))


def option_version(value):
    from . import __version__
    println("pymake3 v{}", __version__)
