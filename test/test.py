#---------------------------------------
# IMPORTS
#---------------------------------------

import sys
sys.path.insert(0, '../src/')

#---------------------------------------
# GLOBALS
#---------------------------------------

_should_fail = False

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def assert_equal(actual, expected, s):
    if actual <> expected:
        print
        print "-----"
        print "TEST FAILED"
        print s
        print "expected:", expected
        print "actual:  ", actual
        print "-----"
        test_fail()

def assert_false(a, s):
    if a:
        print "-----"
        print "TEST FAILED"
        print s
        print "value should be false"
        print "-----"
        test_fail()

def assert_not_equal(a, b, s):
    if a == b:
        print "-----"
        print "TEST FAILED"
        print s
        print "values should not be equal"
        print "-----"
        test_fail()

def assert_true(a, s):
    if not a:
        print "-----"
        print "TEST FAILED"
        print s
        print "value should be true"
        print "-----"
        test_fail()

def test_fail(reason=None):
    if reason:
        print "-----"
        print "TEST FAILED"
        print reason
        print "-----"

    sys.exit(0 if _should_fail else -1)


def test_pass():
    sys.exit(-1 if _should_fail else 0)

def test_should_fail():
    global _should_fail
    _should_fail = True
