#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

from pymake2                 import report
from pymake2.core.exceptions import NoSuchTargetError, NoTargetToMakeError
from pymake2.core.maker      import Maker
from pymake2.core.options    import Options
from pymake2.core.target     import Target
from pymake2.utils           import color

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Exit code when a fatal error has been encountered.
EXIT_FATAL = -1

# Exit code all went well.
EXIT_SUCCESS = 0

#---------------------------------------
# GLOBALS
#---------------------------------------

# Pymake exit code.
exit_code = 0

# Pymake options.
options = Options()

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def fatal(s, *args):
    s = "fatal: " + s.format(*args)

    if not options.no_color:
        s = color.red(s)

    println(s)
    sys.exit(EXIT_FATAL)

def print_targets():
    if len(Maker.inst().targets) == 0:
        return

    println("Targets:")

    max_len = 0

    for target in Maker.inst().targets:
        # Add one since we also add a space or an asterisk to the target name
        # when printing it.
        max_len = max(len(target.name)  + 1, max_len)

    s1 = " {: <" + str(max_len) + "}"
    s2 = s1 + " - {}"
    for target in Maker.inst().targets:
        default = target is Maker.inst().def_target
        desc    = target.desc
        name    = " " + target.name if not default else "*" + target.name

        println(s2 if desc else s1, name, desc)

def print_usage():
    name = os.path.split(sys.argv[0])[1]
    s    = "[target]" if Maker.inst().def_target else "<target>"

    println(
"""
Usage: python {} [options] {}

Options:
  --help     - display information about pymake2
  --no-color - disable text color
  --no-exit  - do not exit automatically after making
  --no-warn  - do not display warnings
  --version  - show pymake2 version
""", name, s)

def print_version():
    from . import __version__
    println("pymake2 v{}", __version__)

def println(s, *args):
    if s:
        s = s.format(*args)
        print s
    else:
        print

def pymake2(conf=None, args=None):
    try:
        pymake2_(conf, args)

    except NoSuchTargetError as e:
        fatal("no such target: {}", e.target_name)

    except NoTargetToMakeError:
        fatal("no target set and there is no default target")

def pymake2_(conf=None, args=None):
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

    Maker.inst().check_targets()

    report_problems()

    if not name and not Maker.inst().def_target:
        raise NoTargetToMakeError()

    Maker.inst().make(name, conf)

    if not options.no_exit:
        sys.exit(exit_code)

def report_problems():
    any_errors = False

    # Report all problems
    for problem in report.problems():
        if problem.is_error:
            any_errors = True

        s = problem.text

        if not options.no_color:
            if problem.is_error: s = color.red   (s)
            else               : s = color.yellow(s)

        if problem.is_error or not options.no_warn:
            println(s)

    if any_errors:
        fatal("there were errors - aborting")
