#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import subprocess

from test    import *
from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------


#---------------------------------------
# SCRIPT
#---------------------------------------

cwd = os.getcwd()
for s in find_files(os.path.join('..', 'examples'), '*make.py'):
    path, filename = os.path.split(s)

    os.chdir(os.path.join(cwd, path))
    r = subprocess.call(['python', filename])

    if r != 0:
        test_fail('example is broken: ' + s)
