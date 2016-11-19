#---------------------------------------
# IMPORTS
#---------------------------------------

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
    """

    pass

@target
def clean(conf):
    """
    Cleans the build by removing the bin directory and all its contents.
    """

    remove_dir(conf.bindir)

def defaultConf():
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
def compile(conf):
    """
    This target compiles the executable program from its sources in the src
    directory.
    """

    create_dir(conf.bindir)

    flags   = conf.flags
    libdirs = ['/lib:' + ','.join(conf.libdirs)]
    libs    = ['/r:' + lib for lib in conf.libs]
    out     = ['/out:' + os.path.join(conf.bindir, conf.name)]
    sources = ['/recurse:' + os.path.join(conf.srcdir, '*.cs')]

    run_program(CSC, flags + libdirs + libs + out + sources)

@target
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
    # If this file is executed directly, run pymake with the default
    # configuration.
    pymake(defaultConf())
