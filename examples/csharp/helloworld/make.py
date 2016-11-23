#!/usr/bin/env python

#---------------------------------------
# IMPORTS
#---------------------------------------

# We need to insert the path to pymake so we can import it first.
import os, sys

# This weird path can be removed if using this make script. It's only needed to
# be able to run the script directly in the source tree.
sys.path.insert(0, os.path.join('..', '..', '..', 'src'))

from pymake import *

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(desc="delete the compiled executable")
def clean(conf):
    delete_file(conf.name)

@default_target(desc="compile HelloWorld.cs into an executable program")
def compile(conf):
    create_dir(conf.bindir)

    flags   = conf.flags
    libdirs = [ '/lib:'     + ','.join(conf.libdirs)               ]
    libs    = [ '/r:'       + lib for lib in conf.libs             ]
    out     = [ '/out:'     + os.path.join(conf.bindir, conf.name) ]
    sources = [ '/recurse:' + os.path.join(conf.srcdir, '*.cs')    ]

    run_program(r'C:\Program Files (x86)\MSBuild\14.0\Bin\csc.exe',
                flags + libdirs + libs + out + sources)

#---------------------------------------
# SCRIPT
#---------------------------------------

# The configuration below depends on the backend used for the make process.  In
# this case, we're using csc, which uses the options set below, among others.
pymake({ 'name': 'HelloWorld.exe',

         # Flags to pass to the compiler.
         'flags': ['/nologo',
                   '/optimize',
                   '/target:exe',
                   '/platform:anycpu'],

         'libdirs': [ r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319' ],

         # These are the libraries referenced by the program.  We can also add
         # the libdirs setting to add directories to look in for libraries
         # during compilation.
         'libs': [ 'System.dll' ],

         # Output the executable into the current directory. If we changed this
         # to 'bin', a directory named bin would be created, and the compiled
         # executable would be stored in it.
         'bindir': '.',

         # We have our source files in the current directory in this example.
         # More source could be added in the source directory, and they would
         # all beautomatically compiled by pymake.
         'srcdir': '.' })
