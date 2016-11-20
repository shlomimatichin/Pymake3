# Pymake Manual

### Table of Contents

1. [Configuring your project](#configuring-your-project)
2. [Writing make scripts](#writing-make-scripts)
3. [Making your projects](#making-your-projects)

## Configuring your project

To use pymake in your projects, at the very least, you need to download and store a copy of `pymake.py` in your project somewhere. pymake should normally be stored in `build/pymake`, but this can be configured if needed. If you intend to use one of the templates for your project, you need to make a decision:

1. Modify the template script as needed for your project and store it in your project root, for example `make.py`.
2. Write your own, separate make script and import the template script from it. In this case, you should store the template file together with `pymake.py` for easy access from your own make script.

When you have saved the needed files into your project, you can run pymake on it by invoking your make script in the project root. If, for example, you saved your script to `make.py`, begin making your project by typing `python make.py` in your project root. Alternatively, you can just type `./make.py` if you're using Linux.

## Writing make scripts

Make scripts for pymake are written in the Python language. For the sake of clarity, we discuss a few aspects of pymake individually before presenting a complete make script.

Firstly, you should place `pymake.py` in build/pymake/ in your project folder. Then, pymake can be imported in the following way:

```python
import sys
sys.path.insert(0, 'build/pymake')
from pymake import *
```

After this, we can start building the make script by defining our targets. Defining a target is trivial:

```python
@target
def my_target(conf):
    print 'hello from my_target!'
```

That's it! That is all that is needed for pymake to register your target and be able to invoke it. Some targets need to be sure that other targets have been completed first. For example, before linking an executable, we need to compile it. This can be achieved easily by specifying dependencies on your targets:

```python
@target
def compile(conf):
    print 'compiling', conf.name

@target
@depends_on('compile')
def link(conf):
    print 'linking', conf.name
```

By specifying dependencies, you ensure that they will always be completed before your target is invoked. In the case above, the compile target will always be invoked before the link target.

At the end of your make script, you need to begin the make process by calling the `pymake()` function. Normally, you want to pass a configuration object to the function and use it in your targets. In this example, we pass in a name since we used it in the target examples above:

```python
pymake({ 'name': 'my_program' })
```

As we now have a basic understanding of how pymake operates, let's look at a more complex make script. Read the comments carefully.

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
    # Pymake passes the configuration in the conf parameter, where each setting
    # is an attribute.  For example, we can print the name setting in the
    # following way:
    print 'name is', conf.name

    # Note that the attributes depend on the configuration passed to pymake.
    # pymake does not care about your configuration and will only pass it on to
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
    # automatically compiled by pymake.
    'srcdir': '.'
})
```

As you can tell by now, pymake is almost infinitely flexible and can be used for any kind of project.

## Making your projects

When you have written your make script and saved `pymake.py` in your project folder, you can make your project easily by invoking your make script.

If, for example, you saved your script to `make.py` in your project root, you can run it by typing `python make.py` to make the `all` target. If you want to specify what target to make, you can type `python make.py my_target_name`. Dependencies will automatically be resolved, so even if you attempt to invoke the `link` target from the examples above, the `compile` target will be invoked before it.

Happy making!
