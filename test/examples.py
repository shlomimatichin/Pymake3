#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import subprocess

import test

from pymake import *

#---------------------------------------
# SCRIPT
#---------------------------------------

cwd = os.getcwd()
for s in find_files(os.path.join('..', 'examples'), '*make.py'):
    path, filename = os.path.split(s)

    os.chdir(os.path.join(cwd, path))
    r = subprocess.call(['python', filename])

    if r != 0:
        test.fail('example is broken: ' + s)

test.success()
