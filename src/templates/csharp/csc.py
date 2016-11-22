"""
Template makke script for Microsoft's C# compiler csc.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os

from pymake import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

CSC = r'C:\Program Files (x86)\MSBuild\14.0\Bin\csc.exe'

#---------------------------------------
# FUNCTIONS
#---------------------------------------

@target
@depends_on('compile')
def all(conf):
    """
    The 'all' target does not do anything on its own.  Instead, it depends on
    other targets that are needed to complete make process.

    :param conf: Make configuration.
    """

    pass

@target
def clean(conf):
    """
    Cleans the build by deleting the bin directory and all its contents.

    :param conf: Make configuration.
    """

    delete_dir(conf.bindir)

@target
def compile(conf):
    """
    This target compiles the executable program from its sources in the source
    directory.

    :param conf: Make configuration.
    """

    create_dir(conf.bindir)

    flags   = conf.flags
    libdirs = ['/lib:' + ','.join(conf.libdirs)]
    libs    = ['/r:' + lib for lib in conf.libs]
    out     = ['/out:' + os.path.join(conf.bindir, conf.name)]
    sources = ['/recurse:' + os.path.join(conf.srcdir, '*.cs')]

    run_program(CSC, flags + libdirs + libs + out + sources)

def default_conf():
    """
    Gets the default configuration.

    :return: Default configuration settings.
    """
    return {
        'name': 'Program.exe',

        'flags': ['/nologo'],

        'libs': [],

        'libdirs': [r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319',
                    r'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF'],

        'bindir': 'bin',
        'srcdir': 'src'
    }

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
    pymake(default_conf())
