Pymake2 Manual
##############

.. contents:: Table of Contents
   :backlinks: none

.. section-numbering::


Guide
=====

Configuring your project
------------------------

To use pymake2 in your projects, download the latest pymake2 release and store the binary file in your project. Normally, pymake2 should be stored in a build directory in your project root, but this can be configured.

You also need to write a make script. To get started quickly, you could take a look at one of the `examples <examples>`_

When you have saved pymake2 and your make script into your project directory, you can run it by invoking your make script in the project root. If, for example, you saved your script to `make.py`, begin making your project by typing `python make.py` in your project root. Alternatively, you can just type :code:`./make.py` if you're using Linux.

Writing make scripts
--------------------

Make scripts for pymake2 are written in the Python programming language. For the sake of clarity, we discuss a few aspects of pymake2 individually before presenting a complete make script.

Firstly, you should place pymake2 in the build directory in your project root. Then, pymake2 can be imported into your make script in the following way:

.. code-block:: python

   import sys
   sys.path.insert(0, 'build/pymake2')
   from pymake2 import *

After this, we can start building the make script by defining our targets. Defining a target is trivial:

.. code-block:: python

   @target
   def my_target(conf):
       print 'hello from my_target!'

That's it! That is all that is needed for pymake2 to register your target and be able to make it. Some targets need to be sure that other targets have been completed first. For example, before linking an executable, we need to compile it. This can be achieved easily by specifying dependencies on your targets:

.. code-block:: python

   @target
   def compile(conf):
       print 'compiling', conf.name

   @target
   @depends_on('compile')
   def link(conf):
       print 'linking', conf.name

By specifying dependencies, you ensure that they will always be completed before a target is made. In the case above, the compile target will always be made before the link target.

At the end of your make script, you need to begin the make process by calling the :code:`pymake2()` function. Normally, you want to pass a configuration object to the function and use it in your targets. In this example, we pass in a name since we used it in the target examples above:

.. code-block:: python

   pymake2({ 'name': 'my_program' })

As we now have a basic understanding of how pymake2 operates, let's look at a more complex make script. Read the comments carefully.

.. code-block:: python

   #!/usr/bin/env python

   import os, sys

   # We need to insert the path to pymake2.py below to be able to import it.  In
   # this script, pymake2 is expected to be located in build/pymake2/.
   sys.path.insert(0, os.path.join('build', 'pymake2'))
   from pymake2 import *

   # Import the C# template for csc.exe.
   from pymake2.template.csharp import csc

   @target
   def my_first_target(conf):
       # Pymake2 passes the configuration in the conf parameter, where each setting
       # is an attribute.  For example, we can print the name setting in the
       # following way:
       print 'name is', conf.name

       # Note that the attributes depend on the configuration passed to pymake2.
       # Pymake2 does not care about your configuration and will only pass it on to
       # your targets as you provided it.
       pass

   # We can specify targets that depend on other targets, as below.  The
   # dependencies will always be invoked before this target is invoked.
   #     Although we use the @depends_on decorator below, we could also have typed
   # @target(depends=[ 'my_first_target' ])
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
   pymake2({
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
       # automatically compiled by pymake2.
       'srcdir': '.'
   })

As you can tell by now, pymake2 is almost infinitely flexible and can be used for any kind of project.

Making your projects
--------------------

When you have written your make script and saved pymake2 in your project build directory, you can make your project easily by invoking your make script.

If, for example, you saved your script to make.py in your project root, you can run it by typing :code:`python make.py` to make the default target if there is one. If you want to specify what target to make, you can type :code:`python make.py my_target_name`. Dependencies will automatically be resolved, so even if you attempt to invoke the :code:`link` target from the examples above, the :code:`compile` target will be invoked before it.

If you are unsure what targets are available, just type :code:`python make.py --targets` to see a list of them.

Quick Reference
===============

Copying files/directories
-------------------------

Copying files (for example, copying resource files to the bin directory when building an executable) can easily be done with the :code:`copy()` function:

.. code-block:: python

   @target
   def copy_assets(conf):
       num = copy(conf.assetsdir, conf.bindir, '*.wav')
       trace('{} files copied', num)

If a directory path is passed to the :code:`copy()` function, that directory is copied recursively to the target path. If the source path is a file, that file will be copied. Optionally, a filename pattern can be specfied, as in the case above. Only files matching the pattern will be copied.

Creating directories
--------------------

Directories are created with the :code:`create_dir()` function:

.. code-block:: python

   @target
   def compile(conf):
       create_dir(conf.bindir)
       # ...

The directory will be created if it does not already exist.

Defining a target
-----------------

A pymake2 target is defined by applying the `@target` decorator to a function:

.. code-block:: python

   @target
   def my_target(conf):
       # ...

A target function always takes in a :code:`conf` argument containing the pymake2 configuration. The target's name is the name of the function, unless another name is
specified:

.. code-block:: python

   @target(name='a_target')
   def my_target(conf):
       # ...

The configuration can be set to a default for each target:

.. code-block:: python

   @target(conf={ text: 'foo'  })
   def my_target(conf):
       print conf.text # Prints 'foo' unless the user provided configuration
                       # overrides it with some other value.

Deleting directories
--------------------

Delete directories with the :code:`delete_dir()` function:

.. code-block:: python

   @target
   def clean(conf):
       delete_dir(conf.bindir)
       delete_dir(conf.objdir)

Deleting files
--------------

Files can be deleted with the :code:`delete_file()` function:

.. code-block:: python

   @target
   def clean(conf):
       delete_file('my_file.xyz')

Finding files
-------------

Files can be found with the :code:`find_files()` function, when you, for example, need to find all source files to compile:

.. code-block:: python

   @target
   def compile(conf):
       sources = find_files(conf.srcdir, '*.c')
       # ...


Running programs
----------------

Run programs with the :code:`run_program()` function:

.. code-block:: python

   @target
   def compile(conf):
       run_program('g++', ['hello.cpp', '-o', 'hello'])

Specifying dependencies
-----------------------

Pymake2 targets can depend on other targets. Dependencies are specified with the :code:`@depends_on` decorator:

.. code-block:: python

   @target
   @depends_on('my_target')
   def my_other_target(conf):
       # my_target will always be invoked before we reach this point

Templates
=========

Pymake2 comes with several ready-made templates for making different kinds of projects. The templates vary greatly depending on area of use, and therefore have their own documentation. Below is a list of the templates; click on one to read more about it.

C#
--
* `csc <templates/csharp/csc.rst>`_

LaTeX
-----
* `pdflatex <templates/latex/pdflatex.rst>`_

Utility
-------
* `fswatcher <templates/util/fswatcher.rst>`_
