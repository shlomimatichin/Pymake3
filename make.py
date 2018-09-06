#!/usr/bin/python3
import os
import py_compile
import sys

sys.path.insert(0, 'src')

from pymake3 import *

CONF={ 'srcdir': 'src',
       'builddir': 'src/build',
       'distdir': 'src/dist',
       'egginfodir': 'src/pymake3.egg-info',
       'target': 'pymake3' }


@default_target(conf=CONF, desc="builds the pymake3 egg package")
def build(conf):
    os.chdir(conf.srcdir)
    run(['python3', 'setup.py', 'bdist_wheel', 'sdist'])


@target(conf=CONF)
def clean(conf):
    for s in [conf.builddir, conf.distdir, conf.egginfodir]:
        delete_dir(s)
    for s in find_files(conf.srcdir, '__pycache__'):
        delete_dir(s)


@target(conf=CONF)
def upload(conf):
    run('twine upload --repository-url=https://test.pypi.org/legacy/ %s/*' % conf.distdir, mode='shell')


pymake3()
