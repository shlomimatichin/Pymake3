#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

from pymake2                 import report
from pymake2.core.exceptions import NoSuchTargetError
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
EXIT_MAKE_OK = 0

# Exit code when there was nothing to do.
EXIT_NO_MAKE = 1

#---------------------------------------
# GLOBALS
#---------------------------------------

# Pymake exit code.
exit_code = EXIT_MAKE_OK

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
    targets = sorted(Maker.inst().targets, key=lambda t: t.name)

    if len(targets) == 0:
        return

    println("Targets:")

    n = 0

    for target in targets:
        # Add one since we also add a space or an asterisk to the target name
        # when printing it.
        n = max(len(target.name) + 1, n)

    s1 = " {: <" + str(n) + "}"
    s2 = s1 + " -"

    maxlen = 72 - n

    for target in targets:
        default = target is Maker.inst().def_target
        desc    = target.desc
        name    = " " + target.name if not default else "*" + target.name

        s = s2 if desc else s1
        print s.format(name),

        if desc:
            words = desc.split(' ')
            desc = ''
            while len(words) > 0:
                while len(words) > 0 and len(desc) + len(words[0]) < maxlen:
                    desc += words[0] + " "
                    words = words[1:]

                print desc
                desc = ' ' * (n + 4)
        else:
            print

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
  --targets  - show available targets
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
    args = sys.argv if args is None else [sys.argv[0]] + args

    # Keep arguments beginning with two hyphens.
    opts = [arg for arg in args if arg.startswith('--')]

    # Keep arguments *not* beginning with two hyphens.
    args = [arg for arg in args if arg not in opts]
    name = args[1] if len(args) > 1 else None
    conf = conf    if conf          else {}

    do_not_make = False

    # Parse command line options.
    for opt in opts:
        if opt == '--help':
            print_usage()
            do_not_make = True
        elif opt == '--targets':
            print_targets()
            do_not_make = True
        elif opt == '--version':
            print_version()
            do_not_make = True
        elif not options.parse(opt):
            report.warn("unknown option: {}", opt)

    Maker.inst().check_targets()

    report_problems()

    if do_not_make:
        return

    if not name and not Maker.inst().def_target:
        println("\nNo target specified and there is no default target.\n")
        print_targets()

        if not options.no_exit:
            sys.exit(EXIT_NO_MAKE)

        return

    try:
        Maker.inst().make(name, conf)
    except NoSuchTargetError as e:
        fatal("no such target: {}", e.target_name)

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
