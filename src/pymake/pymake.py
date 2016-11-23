#---------------------------------------
# IMPORTS
#---------------------------------------

import sys

from core          import color
from core.settings import Settings
from core.target   import Target

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Exit code when a fatal error has been encountered.
EXIT_FATAL = -1

# Exit code all went well.
EXIT_SUCCESS = 0

# Pymake version.
VERSION = '0.42b'

#---------------------------------------
# CLASSES
#---------------------------------------

class Pymake(object):
    def __init__(self):
        self.def_target = None       # Default target.
        self.problems   = []         # List with errors and warnings.
        self.settings   = Settings() # Pymake settings.
        self.targets    = []         # List with known targets.

    def get_target(self, name):
        for target in self.targets:
            if target.name == name:
                return target

        target = Target(name)

        self.targets.append(target)

        return target

    def make(self, name, conf, completed=None):
        if completed is None:
            completed = []

        if name in completed:
            return

        target = self.get_target(name) if name else self.def_target

        if not target.func:
            fatal("no such target: '{}'", name)

        for depend in target.depends:
            self.make(depend, conf, completed)

        target.make(conf)
        completed.append(name)

#---------------------------------------
# GLOBALS
#---------------------------------------

inst = Pymake()

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def error(s, *args):
    inst.problems.add(("error: " + s.format(*args), 'error'))

def fatal(s, *args):
    println(color.red('fatal: ' + s), *args)
    sys.exit(EXIT_FATAL)

def print_usage():
    println(
"""
Usage: [options] [target]

Options:
  --no-color - disable color
  --version  - show pymake version
"""
    )

def println(s, *args):
    if s:
        s = s.format(*args)
        print s
    else:
        print

def pymake(conf=None, args=None):
    args = sys.argv if args is None else [sys.argv[0]] + args

    # Keep arguments beginning with two hyphens.
    opts = [arg for arg in args if arg.startswith('--')]

    # Parse command line options.
    for opt in opts:
        if opt == '--version':
            println('pymake v{}', VERSION)
            return

        if not inst.settings.parse(opt):
            warn("unknown option: {}", opt)

    # Keep arguments *not* beginning with two hyphens.
    args = [arg for arg in args if arg not in opts]
    name = args[1] if len(args) > 1 else None
    conf = conf    if conf          else {}

    if not name and not inst.def_target:
        fatal("no target specified and there is no default target")

    for s, t in inst.problems:
        if not inst.settings.disable_colors:
            if t == 'error': s = color.red   (s)
            else           : s = color.yellow(s)

        if t != 'warning' or not inst.settings.disable_warnings:
            println(s)

    inst.make(name, conf)

def warn(s, *args):
    inst.problems.append(("warning: " + s.format(*args), 'warning'))
