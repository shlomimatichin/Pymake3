"""
Template make script for pdflatex.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import time

from pymake2 import *

#---------------------------------------
# CONSTANTS
#---------------------------------------

CONF={ 'bindir' : 'bin',
       'flags'   : [ '-file-lin-errors', '-halt-on-error' ],
       'srcdir'  : 'src',
       'srcfile' : 'main.tex' }

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

    bindir = os.path.abspath(conf.bindir)
    srcdir = os.path.abspath(conf.srcdir)

    flags      = conf.flags
    job_name   = '-jobname ' + conf.name
    output_dir = '-output-directory ' + os.path.relpath(bindir, srcdir)
    srcfile    = conf.srcfile

    cwd = os.getcwd()

    os.chdir(srcdir)

    run_program('pdflatex', flags + [job_name] + [output_dir] + [srcfile])

    os.chdir(cwd)

@target(conf=CONF)
def watch(conf):
    """
    This target automatically invokes the 'compile' target after changes have
    been detected in the source file.

    :param conf: Make configuration.
    """

    filenames = find_files(conf.srcdir, '*.tex') + find_files(conf.srcdir, '*.bib')

    mtimes = {}

    while True:
        files_changed = False

        for filename in filenames:
            if not os.path.isfile(filename):
                continue

            mtime = os.path.getmtime(filename)

            if not filename in mtimes:
                mtimes[filename] = 0

            if mtime > mtimes[filename]:
                mtimes[filename] = mtime
                files_changed = True

        if files_changed:
            make('compile', conf)

        time.sleep(0.5)

#---------------------------------------
# SCRIPT
#---------------------------------------

if __name__ == '__main__':
    pymake2()
