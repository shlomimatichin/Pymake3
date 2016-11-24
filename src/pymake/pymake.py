#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

from core.options  import Options
from core.target   import Target

import color

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Exit code when a fatal error has been encountered.
EXIT_FATAL = -1

# Exit code all went well.
EXIT_SUCCESS = 0

#---------------------------------------
# CLASSES
#---------------------------------------

class Pymake(object):
    def __init__(self):
        self.def_target = None # Default target.
        self.problems   = []   # List with errors and warnings.
        self.targets    = []   # List with known targets.

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

# Pymake exit code.
exit_code = 0

# Pymake options.
options = Options()

# Pymake instance where most data is stored.
inst = Pymake()

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def error(s, *args):
    inst.problems.add(("error: " + s.format(*args), 'error'))

def fatal(s, *args):
    s = 'fatal: ' + s.format(*args)

    if not options.no_color:
        s = color.red(s)

    println(s)
    sys.exit(EXIT_FATAL)

def print_problems():
    # Notify the user of all problems.
    for s, t in inst.problems:
        if not options.no_color:
            if t == 'error': s = color.red   (s)
            else           : s = color.yellow(s)

        if t != 'warning' or not options.no_warn:
            println(s)

def print_targets():
    if len(inst.targets) == 0:
        return

    println("Targets:")

    max_len = 0

    for target in inst.targets:
        # Add one since we also add a space or an asterisk to the target name
        # when printing it.
        max_len = max(len(target.name)  + 1, max_len)

    s1 = " {: <" + str(max_len) + "}"
    s2 = s1 + " - {}"
    for target in inst.targets:
        default = target is inst.def_target
        desc    = target.desc
        name    = " " + target.name if not default else "*" + target.name

        println(s2 if desc else s1, name, desc)

def print_usage():
    name = os.path.split(sys.argv[0])[1]
    s    = "[target]" if inst.def_target else "<target>"

    println(
"""
Usage: python {} [options] {}

Options:
  --help     - display information about pymake
  --no-color - disable text color
  --no-exit  - do not exit automatically after making
  --no-warn  - do not display warnings
  --version  - show pymake version
""", name, s)

def print_version():
    from . import __version__
    println("pymake v{}", __version__)

def println(s, *args):
    if s:
        s = s.format(*args)
        print s
    else:
        print

def pymake(conf=None, args=None):
    args = sys.argv if args is None else [sys.argv[0]] + args

    # Keep arguments beginning with two hyphens.
    opts = [arg for arg in args if arg.startswith('-')]

    # Keep arguments *not* beginning with two hyphens.
    args = [arg for arg in args if arg not in opts]
    name = args[1] if len(args) > 1 else None
    conf = conf    if conf          else {}

    # Parse command line options.
    for opt in opts:
        if opt == '--help':
            print_version()
            print_usage()
            print_targets()
            return

        if opt == '--version':
            print_version()
            return

        if not options.parse(opt):
            warn("unknown option: {}", opt)

    if not name and not inst.def_target:
        fatal("no target specified and there is no default target")

    print_problems()

    # Make sure we only show all problems once.
    inst.problems = []

    inst.make(name, conf)

    if not options.no_exit:
        sys.exit(exit_code)

def warn(s, *args):
    inst.problems.append(("warning: " + s.format(*args), 'warning'))
