#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Exit code when a test has failed.
EXIT_FAIL = -1

# Exit code when a test has passed.
EXIT_SUCCESS = 0

#---------------------------------------
# GLOBALS
#---------------------------------------

name = os.path.split(sys.argv[0])[1][:-3]

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def equal(value, expected_value, s):
    if value == expected_value:
        return

    s += '\n{}: expected {} but got {}'.format(name, expected_value, value)

    fail(s)

def false(value, s):
    if value == False:
        return

    fail(s)

def true(value, s):
    if value == True:
        return

    fail(s)

def fail(reason, *args):
    if reason:
        print '{}: test failed: '.format(name) + reason.format(*args)
    else:
        print '{}: test failed'.format(name)

    sys.exit(EXIT_FAIL)

def success():
    sys.exit(EXIT_SUCCESS)

#---------------------------------------
# SCRIPT
#---------------------------------------

sys.path.insert(0, os.path.join('..', 'src'))
