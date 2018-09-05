"""
Provides functionality for access the file system through pymake3 - finding
files, creating, deleting and copying files and directories etc.
  Although all these operations can be performed without pymake3, this module
aims to provide a simple interface for performing them. The goal is to provide a
natural syntax, allowing less experienced users to make use of pymake3 in their
projects.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

import fnmatch
import os
import shutil
import time

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def _def_copy_pred(srcpath, destpath):
    """
    Default file copying predicate. Does not overwrite newer files.

    :param srcpath:  Source path.
    :param destpath: Destination path.

    :return: True if the source file is newer than the destination file.
    """
    if not os.path.exists(destpath):
        return True

    # Only overwrite the file if the source is modified at a later time
    # than the destination.
    src_modified_time  = os.path.getmtime(srcpath)
    dest_modified_time = os.path.getmtime(destpath)

    return src_modified_time >= dest_modified_time

def copy(srcpath, destpath, pattern=None, pred=_def_copy_pred):
    """
    Copies all files in the source path to the specified destination path.  The
    source path can be a file, in which case that file will be copied as long as
    it matches the specified pattern.
        If the source path is a directory, all directories in it will be
    recursed and any files matching the specified pattern will be copied.

    :param srcpath:  Source path to copy files from.
    :param destpath: Destination path to copy files to.
    :param pattern:  Pattern to match filenames against.
    :param pred:     Predicate to decide which files to copy/overwrite.

    :return: Number of files copied.
    """
    if os.path.isfile(srcpath):
        if pattern and not fnmatch.fnmatch(srcpath, pattern):
            return 0

        if pred and pred(srcpath, destpath) == False:
            return 0

        path, filename = os.path.split(destpath)

        if not os.path.exists(path):
            # Make sure all directories needed to copy the file exist.
            create_dir(path)

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
        os.makedirs(path)

def delete_dir(path):
    """
    Deletes the specified directory if it exists.  All files inside the
    directory will be deleted.

    :param path: Path of the directory to delete.

    :return: True if the path was a directory and was deleted.
    """
    if os.path.isdir(path):
        shutil.rmtree(path)
        return True

    return False

def delete_file(path):
    """
    Deletes the specified file if it exists.

    :param path: Path of the file to delete.

    :return: True if the path was a file and was deleted.
    """
    if os.path.isfile(path):
        os.remove(path)
        return True

    return False

def find_files(path, pattern=None):
    """
    Finds all files in the specified directory that match the specified
    pattern.

    :param path:    Path to a directory to search for files in.
    :param pattern: Pattern to match filenames against. Can be an iterable to
                    specify more than one pattern.

    :return: A list containing all files in the path that matches the pattern.
    """
    filenames = []

    for s in os.listdir(path):
        s = os.path.join(path, s)

        if os.path.isfile(s):
            if pattern is None:
                filenames.append(s)
            elif isinstance(pattern, str):
                if fnmatch.fnmatch(s, pattern):
                    filenames.append(s)
            else:
                for p in pattern:
                    if fnmatch.fnmatch(s, p):
                        filenames.append(s)
                        break

        else:
            filenames.extend(find_files(s, pattern))

    return filenames

def watch_files(filenames, cb, arg=None, interval=0.5):
    """
    Watches the specified list of files for changes, invoking the callback
    function as soon as a change has been detected in one of the files.

    :param filenames: Array containing names of files to watch.
    :param cb:        Callback function to invoke when changes have been
                      detected.
    :param arg:       Argument to pass to the callback function along with names
                      of files that have changed.
    :param interval:  Delay to wait between each poll for changes, in seconds.
    """
    changed_files = []
    mtimes = {}

    for filename in filenames:
        mtimes[filename] = 0

    while cb(arg, changed_files):
        changed_files = []

        for filename in filenames:
            # Maybe the file has been deleted?
            if not os.path.isfile(filename):
                continue

            mtime = os.path.getmtime(filename)

            if mtime != mtimes[filename]:
                # This file has had its 'modified time' attribute updated.
                mtimes[filename] = mtime
                changed_files.append(filename)

        time.sleep(interval)
