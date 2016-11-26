Template: `fswatcher </src/pymake2/template/util/fswatcher.py>`_
################################################################

What does the fswatcher template do?
------------------------------------
The fswatcher template provides the `watch` target, which watches files in a
directory for changes. When a change has been detected, fswatcher makes a
specified target.

Use the fswatcher template to, for example, automatically compile a program or
document as soon as a change is detected in one of the source files. This way,
you can live-preview your documents as you modify them.

Targets
-------
* :code:`watch` - Watches files in a directory for changes, making a specified target when a change has been detected in any of the files.

Default configuration
---------------------

.. code-block:: python

   { 'fswatcher': {
         # List of file extensions to watch.  Only files matching any of the
         # file extensions will trigger fswatcher.
         'extensions': [ '*.*' ],

         # Delay, in seconds, between each poll for file changes.
         'interval': 0.5,

         # Path to watch for file changes.  Only files in this path will trigger
         # fswatcher.
         'path': 'src',

         # Target to make when a file change has been detected.
         'target': 'compile'
     } }

Example
-------
.. code-block:: python

   import os, sys
   sys.path.insert(0, os.path.join('build', 'pymake2'))

   from pymake2 import *
   from pymake2.template.util import fswatcher

   fswatcher.conf.fswatcher.target = 'my_target'

   @target
   def my_target(conf):
       print "a file has been changed in the 'src' directory!"

   pymake2()
