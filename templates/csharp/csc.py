"""
Template make script for Microsoft's C# compiler csc.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os

from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

# Path to the csc compiler to use.
CSC = r'C:\Program Files (x86)\MSBuild\14.0\Bin\csc.exe'

# Path to the .NET framework.
DOTNET = r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319'

# Default configuration settings.
CONF = { 'bindir'  : 'bin',
         'flags'   : [ '/nologo' ],
         'libs'    : [],
         'libdirs' : [ DOTNET, os.path.join(DOTNET, 'WPF') ],
         'name'    : 'Program.exe',
         'srcdir'  : 'src' }

# The default csc compiler specified is the one included with Visual Studio 15.
# If it doesn't exist, fall back to the one included with the .NET framework
# version 4.5.
if not os.path.isfile(CSC):
    CSC = os.path.join(DOTNET, 'csc.exe')

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target(conf=CONF, default=True, depends=[ 'compile' ])
def all(conf):
    """
    The 'all' target does not do anything on its own.  Instead, it depends on
    other targets that are needed to complete make process.

    :param conf: Make configuration.
    """

    pass

@target(conf=CONF)
def clean(conf):
    """
    Cleans the build by deleting the bin directory and all its contents.

    :param conf: Make configuration.
    """

    delete_dir(conf.bindir)

@target(conf=CONF)
def compile(conf):
    """
    This target compiles the executable program from its sources in the source
    directory.

    :param conf: Make configuration.
    """

    create_dir(conf.bindir)

    flags   = conf.flags
    libdirs = [ '/lib:'     + ','.join(conf.libdirs)               ]
    libs    = [ '/r:'       + lib for lib in conf.libs             ]
    out     = [ '/out:'     + os.path.join(conf.bindir, conf.name) ]
    sources = [ '/recurse:' + os.path.join(conf.srcdir, '*.cs')    ]

    if getattr(conf, 'debug', False):
        flags += [ '/debug', '/define:DEBUG' ]

    if getattr(conf, 'optimize', False):
        flags += [ '/o' ]

    run_program(CSC, flags + libdirs + libs + out + sources)

@target
def run(conf):
    """
    Runs the target executable.  This target has no dependencies, so the program
    needs to be built first.

    :param conf: Make configuration.
    """

    os.chdir(conf.bindir)
    run_program(conf.name)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    # If this script is executed directly, run pymake with the default
    # configuration.
    pymake()
