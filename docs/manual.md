# PyMake Manual

## Using PyMake

### Configuring your project

To use PyMake in your projects, at the very least, you need to download and store a copy of `pymake.py` in your project somewhere. The default location that PyMake is configured for is `build/pymake`, but this can be configured. If you intend to use one of the templates for your project, you need to make a decision:

1. Modify the template script as needed for your project and store it in your project root, for example `make.py`.
2. Write your own, separate make script and import the template script from it. In this case, you should store the template file together with `pymake.py` for easy access from your own make script.

When you have saved the needed files into your project, you can run PyMake on it by invoking your make script in the project root. If, for example, you saved your script to `make.py`, begin making your project by typing `python make.py` in your project root. Alternatively, you can just type `./make.py` if you're using Linux.

### Writing make scripts

The make scripts are written in Python. For the sake of clarity, we provide a make script example below and discuss it before delving into details:

```python
#!/usr/bin/env python

import os, sys

# We need to insert the path to pymake.py below to be able to import it.  In
# this script, pymake.py is expected to be located in build/pymake/.
sys.path.insert(0, os.path.join('build', 'pymake'))
from pymake import *

# Here, we import the C# template for csc.exe.  Python is going to look for it
# in the same directory as pymake.py, so csc.py needs to be there as well.
# Without this line, we would have no template base. That's ok, but then we
# would have to write all our targets in this file.
import csc

# We can also specify targets by using the @target decorator.
@target
def my_first_target(conf):
    # PyMake passes the configuration in the conf parameter, where each setting
    # is an attribute.  For example, we can print the name setting in the
    # following way:
    print 'name is', conf.name

    # Note that the attributes depend on the configuration passed to PyMake.
    # PyMake does not care about your configuration and will only pass it on to
    # your targets as you provided it.
    pass

# We can specify targets that depend on other targets, as below.  The
# dependencies will always be invoked before this target is invoked.
@target
@depends_on('my_first_target')
def my_second_target(conf):
    print 'my second target will always be invoked *after* my first target!'

# The csc template provides the target 'compile', among others.  If we wanted to
# replace it, we can specify it again here.  It will overwrite the target that
# we imported with 'import csc'.
@target
def compile(conf):
    # This target will replace the target in the csc template.  We can still
    # invoke the target from the template, if we, for example, wanted to wrap
    # the target with more functionality.
    print 'now calling csc.compile'
    csc.compile(conf)

# The configuration below depends on the backend used for the make process.  In
# this case, we're using csc, which uses the settings below, among others.
pymake(csc.defaultConf(), {
    'name': 'HelloWorld.exe',

    'flags': ['/target:exe',
              '/o',
              '/platform:anycpu'],

    # These are the libraries referenced by the program.  We can also add the
    # libdirs setting to add directories to look in for libraries during
    # compilation.  Again, this is dependent on your targets.
    'libs': ['System.dll'],

    # Output the executable into the current directory. If we changed this to
    # 'bin', a directory named bin would be created, and the compiled executable
    # would be stored in it.
    'bindir': '.',

    # We have our source files in the current directory in this example.  More
    # source could be added in the source directory, and they would all be
    # automatically compiled by PyMake.
    'srcdir': '.'
})
```

As you can see, PyMake is almost infinitely flexible and can be used for any
kind of project.
