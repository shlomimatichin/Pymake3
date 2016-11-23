#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import subprocess
import time

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def run_all_tests():
    print 'running tests...'
    print

    failing = []
    passing = []

    start_time = time.time()

    for filename in os.listdir('.'):
        if not filename.endswith('.py'):
            continue

        if filename == 'runtests.py' or filename == 'test.py':
            continue

        test_name = filename[:-3]

        print "running test:", test_name
        r = subprocess.call(['python', filename])

        if r:  failing.append(test_name)
        else:  passing.append(test_name)

    end_time = time.time()

    num_tests = len(passing) + len(failing)

    t = "{:.2}".format(end_time - start_time)

    print
    print "ran", num_tests, "tests in", t, "seconds"
    print
    print "results:"
    print
    print "passing ({}):".format(len(passing))
    print " ".join(passing)

    if len(failing) > 0:
        print
        print "failing ({}):".format(len(failing))
        print " ".join(failing)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    run_all_tests()
