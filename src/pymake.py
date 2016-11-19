#---------------------------------------
# IMPORTS
#---------------------------------------

import fnmatch
import os
import shutil
import subprocess
import sys

#---------------------------------------
# GLOBALS
#---------------------------------------

# Exit code to exit with when done.
exit_code = 0

# Known targets that have been registered with the @target decorator.
targets = {}

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def depends_on(*targets):
    """
    Registers dependencies for a make target.

    :params targets: Names of the dependencies.
    """

    def decorator(func):
        func.dependencies = targets
        return func

    return decorator

def find_files(path, pattern=None):
    """
    Finds all files in the specified directory that match the specified
    pattern.

    :param path:    Path to a directory to search for files in.
    :param pattern: Pattern to match filenames against.
    """

    sources = []

    for s in os.path.listdir(path):
        s = os.path.join(path, s)

        if os.path.isfile(s):
            if not pattern or fnmatch.fnmatch(s, pattern):
                sources.append(s)
        else:
            sources.extend(find_files(s, pattern))

    return sources

def copy(srcpath, destpath, pattern=None):
    """
    Copies all files in the source path to the specified destination path.  The
    source path can be a file, in which case that file will be copied as long as
    it matches the specified mattern. If the source path is a directory, all
    directories in it will be recursed and any files matching the specified
    pattern will be copied.

    :param srcpath:  Source path to copy files from.
    :param destpath: Destination path to copy files to.
    :param pattern:  Pattern to match filenames against.
    """

    if os.path.isfile(srcpath):
        if pattern and not fnmatch.fnmatch(srcpath, pattern):
            return

        if os.path.exists(destpath):
            # Only overwrite the file if the source is modified at a later time
            # than the destination.
            src_modified_time  = os.path.getmtime(srcpath)
            dest_modified_time = os.path.getmtime(destpath)
            if src_modified_time <= dest_modified_time:
                return

        path, filename = os.path.split(destpath)
        trace('copying {} to {}', filename, path)

        if not os.path.exists(path):
            # Make sure all directories needed to copy the file exist.
            os.makedirs(path)

        shutil.copyfile(srcpath, destpath)
        return

    for s in os.listdir(srcpath):
        src  = os.path.join(srcpath , s)
        dest = os.path.join(destpath, s)

        copy(src, dest, pattern)

def create_dir(path):
    """
    Creates the specified directory if it does not exist.

    :param path: Path of the directory to create.
    """

    if not os.path.exists(path):
        os.mkdir(path)

def make(target):
    """
    Attempts to make the specified target, making all its dependencies first.

    :param target: The name of the target to make.
    """

    if target not in targets:
        trace('no such target: {}', target)
        return

    make_func = targets[target]

    if hasattr(make_func, 'dependencies'):
        for dep in make_func.dependencies:
            make(dep)

    trace()
    make_func()

def pymake():
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    make(target)
    sys.exit(exit_code)

def remove_dir(path):
    """
    Removes the specified directory if it exists.  All files inside the
    directory will be removed.

    :param path: Path of the directory to remove.
    """

    if os.path.isdir(path):
        shutil.rmtree(path)

def run_program(s, args):
    """
    Runs the specified program with the specified arguments.

    :param s:    Name of the program to run.
    :param args: Program arguments.
    """

    global exit_code
    exit_code = subprocess.call([s] + args)

    return exit_code

def target(func):
    """
    Marks a function as a make target. The function name will be its name.

    :param func: Function to register as a target.
    """

    targets[func.__name__] = func

    return func

def trace(s=None, *args):
    """
    Displays the specified text, formatted with the specified arguments.

    :param s:     Text to display.
    :param args: Text formatting arguments.
    """

    if not s:
        print
        return

    print s.format(*args)
