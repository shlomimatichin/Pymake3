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
_exit_code = 0

# Known targets that have been registered with the @target decorator.
_targets = {}

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def copy(srcpath, destpath, pattern=None):
    """
    Copies all files in the source path to the specified destination path.  The
    source path can be a file, in which case that file will be copied as long as
    it matches the specified mattern.  If the source path is a directory, all
    directories in it will be recursed and any files matching the specified
    pattern will be copied.

    :param srcpath:  Source path to copy files from.
    :param destpath: Destination path to copy files to.
    :param pattern:  Pattern to match filenames against.

    :return: Number of files copied.
    """

    if os.path.isfile(srcpath):
        if pattern and not fnmatch.fnmatch(srcpath, pattern):
            return 0

        if os.path.exists(destpath):
            # Only overwrite the file if the source is modified at a later time
            # than the destination.
            src_modified_time  = os.path.getmtime(srcpath)
            dest_modified_time = os.path.getmtime(destpath)
            if src_modified_time <= dest_modified_time:
                return 0

        path, filename = os.path.split(destpath)
        trace('copying {} to {}', filename, path)

        if not os.path.exists(path):
            # Make sure all directories needed to copy the file exist.
            os.makedirs(path)

        shutil.copyfile(srcpath, destpath)
        return 1

    num_files_copied = 0

    for s in os.listdir(srcpath):
        src  = os.path.join(srcpath , s)
        dest = os.path.join(destpath, s)

        num_files_copied += copy(src, dest, pattern)

    return num_files_copied

def create_dir(path):
    """
    Creates the specified directory if it does not exist.

    :param path: Path of the directory to create.
    """

    if not os.path.exists(path):
        os.mkdir(path)


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

    :return: A list containing all files in the path that matches the pattern.
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

def make(target, conf):
    """
    Attempts to make the specified target, making all its dependencies first.

    :param target: The name of the target to make.
    """

    if target not in _targets:
        trace('no such target: {}', target)
        return

    make_func = _targets[target]

    if hasattr(make_func, 'dependencies'):
        for dep in make_func.dependencies:
            make(dep, conf)

    trace()
    make_func(conf)

def pymake(*args):
    """
    Starts the make process using the specified configuration.  When the make
    process has completed, exists the script.  The exit code will be the result
    of the last program executed by the make process.

    :param conf: Make configuration.
    """

    # Simple hack to create attributes from the configuration keys.
    final_config = lambda: None

    for conf in args:
        for key, value in conf.iteritems():
            new_value = value
            old_value = getattr(final_config, key, None)

            if old_value:
                if isinstance(old_value, list):
                    new_value.extend(old_value)
                elif isinstance(old_value, tuple):
                    new_value = new_value + old_value

            setattr(final_config, key, new_value)

    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    make(target, final_config)
    sys.exit(_exit_code)

def remove_dir(path):
    """
    Removes the specified directory if it exists.  All files inside the
    directory will be removed.

    :param path: Path of the directory to remove.
    """

    if os.path.isdir(path):
        shutil.rmtree(path)

def run_program(s, args=None):
    """
    Runs the specified program with the specified arguments.

    :param s:    Name of the program to run.
    :param args: Program arguments.

    :return: Exit code returned by the executed program.
    """

    if not args:
        args = []

    global exit_code
    exit_code = subprocess.call([s] + args)

    return exit_code

def target(func):
    """
    Marks a function as a make target. The function name will be its name.

    :param func: Function to register as a target.

    :return: The function passed intp the decorator.
    """

    _targets[func.__name__] = func

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
