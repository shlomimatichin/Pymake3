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

targets = {}

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def find_sources(path, pattern=None):
    sources = []

    for s in os.path.listdir(path):
        s = os.path.join(path, s)

        if os.path.isfile(s):
            if not pattern or fnmatch.fnmatch(s, pattern):
                sources.append(s)
            else:
                sources.extend(find_sources(s, pattern))

    return sources

def copy(srcpath, destpath, pattern=None):
    if os.path.isfile(srcpath):
        if pattern and not fnmatch.fnmatch(srcpath, pattern):
            return

        if os.path.exists(destpath):
            srcmt = os.path.getmtime(srcpath)
            destmt = os.path.getmtime(destpath)
            if srcmt <= destmt:
                return

        path, filename = os.path.split(destpath)
        trace('copying {} to {}', filename, path)

        shutil.copyfile(srcpath, destpath)
        return

    if not os.path.exists(destpath):
        os.makedirs(destpath)

    for s in os.listdir(srcpath):
        dest = os.path.join(destpath, s)
        src = os.path.join(srcpath, s)

        if os.path.isfile(s):
            copy(src, dest, pattern)
        else:
            copy(src, dest, pattern)

def make(target=None):
    if not target:
        target = sys.argv[1] if len(sys.argv) > 1 else 'all'

    if target not in targets:
        trace('no such target {}', target)
        return

    func = targets[target]

    for dep in func.dependencies:
        make(dep)

    trace()
    func()

def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

def run_cmd(s, args):
    subprocess.call([s] + args)

def target(*args):
    def wrapper(func):
        func.dependencies = args
        name = func.__name__
        targets[name] = func
        return func

    return wrapper

def trace(s=None, *args):
    if not s:
        print
        return

    print s.format(*args)
