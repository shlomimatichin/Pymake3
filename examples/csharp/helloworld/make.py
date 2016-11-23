#!/usr/bin/env python

# We need to insert the path to pymake.py so we can import it first.

import os, sys

# Remove these weird paths - they are only here so the examples can be run
# directly in the source tree.
sys.path.insert(0, os.path.join('..', '..', '..', 'src'))
sys.path.insert(0, os.path.join('..', '..', '..', 'templates', 'csharp'))

from pymake import *

import csc

# The configuration below depends on the backend used for the make process.  In
# this case, we're using csc, which uses the options set below, among others.
pymake({
    'name': 'HelloWorld.exe',

    'flags': ['/target:exe',
              '/o',
              '/platform:anycpu'],

    # These are the libraries referenced by the program.  We can also add the
    # libdirs setting to add directories to look in for libraries during
    # compilation.
    'libs': ['System.dll'],

    # Output the executable into the current directory. If we changed this to
    # 'bin', a directory named bin would be created, and the compiled executable
    # would be stored in it.
    'bindir': '.',

    # We have our source files in the current directory in this example.  More
    # source could be added in the source directory, and they would all be
    # automatically compiled by pymake.
    'srcdir': '.'
})
