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

def fail(reason, *args):
    if reason:
        print '{}: test failed: '.format(name) + reason.format(*args)
    else:
        print '{}: test failed'.format(name)

    sys.exit(EXIT_FAIL)

def false(value, s):
    if value == False:
        return

    fail(s)

def should_fail():
    # This method doesn't do anything. It's looked up by the runtests script,
    # to see which tests are expected to fail (i.e. a failure means success).
    pass

def success():
    sys.exit(EXIT_SUCCESS)

def true(value, s):
    if value == True:
        return

    fail(s)

#---------------------------------------
# SCRIPT
#---------------------------------------

sys.path.insert(0, os.path.join('..', 'src'))
