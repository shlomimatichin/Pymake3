"""
Prints information about pymake3 to the user.
"""
#---------------------------------------
# IMPORTS
#---------------------------------------

import os
import sys

from pymake3.core.maker import Maker

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def print_targets():
    targets = sorted(Maker.inst().targets, key=lambda t: t.name)

    if len(targets) == 0:
        return

    print("\nTargets:")

    n = 0

    for target in targets:
        # Add one since we also add a space or an asterisk to the target name
        # when printing it.
        n = max(len(target.name) + 1, n)

    s1 = " {: <" + str(n) + "}"
    s2 = s1 + " -"

    maxlen = 72 - n

    for target in targets:
        default = target is Maker.inst().def_target
        desc    = target.desc
        name    = " " + target.name if not default else "*" + target.name

        s = s2 if desc else s1
        print(s.format(name), end='')

        if desc:
            words = desc.split(' ')
            desc = ''
            while len(words) > 0:
                while len(words) > 0 and len(desc) + len(words[0]) < maxlen:
                    desc += words[0] + " "
                    words = words[1:]

                print(desc)
                desc = ' ' * (n + 4)
        else:
            print('')

    print('')

def print_usage():
    name = os.path.split(sys.argv[0])[1]
    s    = "[target]" if Maker.inst().def_target else "<target>"

    print((
"""
Usage: python {} [options] {}

Options:
  --conf=<s> - set the configuration to use
  --help     - display information about pymake3
  --no-color - disable text color
  --no-exit  - do not exit automatically after making
  --no-warn  - do not display warnings
  --targets  - show available targets
  --version  - show pymake3 version
""").format(name, s))
