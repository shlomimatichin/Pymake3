"""
Provides the command-line interface for pymake3.
"""
#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

from pymake3                 import report
from pymake3.cli             import info, options
from pymake3.core            import makeconf
from pymake3.core.exceptions import NoSuchTargetError
from pymake3.core.maker      import Maker
from pymake3.core.target     import Target
from pymake3.utils           import color

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

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def fatal(s, *args):
    s = "fatal: " + s.format(*args)

    if not options.disable_color:
        s = color.red(s)

    println(s)
    sys.exit(EXIT_FATAL)

def println(s=None, *args):
    if s:
        s = s.format(*args)
        print(s)
    else:
        print()

def pymake3(conf=None, args=None):
    args = sys.argv if args is None else [sys.argv[0]] + args

    # Keep arguments beginning with two hyphens.
    opts = [arg for arg in args if arg.startswith('--')]

    # Keep arguments *not* beginning with two hyphens.
    args = [arg for arg in args if arg not in opts]

    # Parse command line options.
    options.parse(opts)

    if conf and isinstance(conf, dict):
        conf = makeconf.from_dict(conf)

    conf = conf or options.conf or makeconf.from_dict({})

    if options.conf:
        conf = makeconf.merge(conf, options.conf)

    Maker.inst().check_targets()

    report_problems()

    targets = args[1:]
    if not targets:
        targets = [ None ]
    for name in targets:
        if not name and not Maker.inst().def_target:
            println("\nNo target specified and there is no default target.")
            info.print_targets()

            sys.exit(EXIT_NO_MAKE)

        try:
            Maker.inst().make(name, conf)
        except NoSuchTargetError as e:
            fatal("no such target: '{}'", e.target_name)

    #sys.exit(exit_code)

def report_problems():
    any_errors = False

    # Report all problems
    for problem in report.problems():
        if problem.is_error:
            any_errors = True

        s = problem.text

        if not options.disable_color:
            if problem.is_error: s = color.red   (s)
            else               : s = color.yellow(s)

        if problem.is_error or not options.disable_warnings:
            println(s)

    if any_errors:
        fatal("there were errors; aborting.")
