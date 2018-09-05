#!/usr/bin/python3
"""
Template make script for Microsoft's C# compiler csc.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os

from pymake3 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Path to the csc compiler to use.
CSC = r'C:\Program Files (x86)\MSBuild\14.0\Bin\csc.exe'

# Path to the .NET framework.
DOTNET = r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319'

#---------------------------------------
# GLOBALS
#---------------------------------------

# Default configuration settings.
conf = makeconf.from_dict({ 'bindir'  : 'bin',
                            'flags'   : [ '/nologo' ],
                            'libs'    : [],
                            'libdirs' : [ DOTNET, os.path.join(DOTNET, 'WPF') ],
                            'name'    : 'Program.exe',
                            'srcdir'  : 'src' })

# The default csc compiler specified is the one included with Visual Studio 15.
# If it doesn't exist, fall back to the one included with the .NET framework
# version 4.5.
if not os.path.isfile(CSC):
    CSC = os.path.join(DOTNET, 'csc.exe')

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(conf=conf)
def clean(conf):
    """
    Cleans the build by deleting the bin directory and all its contents.
    """
    delete_dir(conf.bindir)

@target(conf=conf)
def compile(conf):
    """
    Compiles the executable program from its sources in the source directory.
    """
    exe_file = os.path.join(conf.bindir, conf.name)

    if os.path.isfile(exe_file):
        mtime = os.path.getmtime(exe_file)
        skip  = True

        for s in find_files(conf.srcdir, '*.cs'):
            if os.path.getmtime(s) > mtime:
                skip = False
                break

        if skip:
            # No source files have changed since the last compile, so we don't
            # need to recompile.
            return

    create_dir(conf.bindir)

    flags   = conf.flags
    libdirs = [ '/lib:'     + ','.join(conf.libdirs)            ]
    libs    = [ '/r:'       + lib for lib in conf.libs          ]
    out     = [ '/out:'     + exe_file                          ]
    sources = [ '/recurse:' + os.path.join(conf.srcdir, '*.cs') ]

    if getattr(conf, 'debug', False):
        flags += [ '/debug', '/define:DEBUG' ]

    if getattr(conf, 'optimize', False):
        flags += [ '/o' ]

    run_program(CSC, flags + libdirs + libs + out + sources)

@target(conf=conf)
def run(conf):
    """
    Runs the target executable.  This target has no dependencies, so the program
    needs to be built first.
    """
    os.chdir(conf.bindir)
    run_program(conf.name)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    pymake3()
