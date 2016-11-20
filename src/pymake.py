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

def check_dependencies(target, dependencies=tuple()):
    """
    Checks the specified target recursively, making sure there are no circular
    dependencies.

    :param target:       Target to check for circular dependencies.
    :param dependencies: Do not specify. Used internally to track dependencies.
    """

    if target not in _targets:
        error('no such target: {}', target)

    if target in dependencies:
        error('circular dependency found while making target: {}', target)

    for dep in get_dependencies(target):
        check_dependencies(dep, (target,) + dependencies)

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

        if not os.path.exists(path):
            # Make sure all directories needed to copy the file exist.
            create_dir(path)

        shutil.copyfile(srcpath, destpath)
        trace('copied {} to {}', srcpath, destpath)

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
        os.makedirs(path)
        trace('created directory {}', path)

def depends_on(*targets):
    """
    Registers dependencies for a make target.

    :params targets: Names of the dependencies.
    """

    def decorator(func):
        func.dependencies = targets
        return func

    return decorator

def error(s, *args):
    """
    Exits pymake with an error message.

    :param s:    Text to display.
    :param args: Text formatting arguments.
    """

    trace('error: ' + s, *args)
    sys.exit(-1)

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

def make(target, conf, completed=[]):
    """
    Attempts to make the specified target, making all its dependencies first.

    :param target:    Name of the target to make.
    :param conf:      Configuration settings.
    :param completed: Used to keep track of previously completed targets
                      during recursion.
    """

    if target in completed:
        return

    make_func = _targets[target]

    for dependency in get_dependencies(target):
        make(dependency, conf, completed)

    make_func(conf)
    completed.append(target)

    trace()

def get_dependencies(target):
    if target not in _targets:
        error('no such target: {}', target)

    make_func = _targets[target]

    if not hasattr(make_func, 'dependencies'):
        return []

    return make_func.dependencies

def pymake(*args):
    """
    Starts the make process using the specified configuration.  When the make
    process has completed, exists the script.  The exit code will be the result
    of the last program executed by the make process.

    :param conf: Make configuration.
    """

    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    check_dependencies(target)

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
        trace('removed directory {}', path)

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

    :param s:    Text to display.
    :param args: Text formatting arguments.
    """

    if not s:
        print
        return

    print s.format(*args)
