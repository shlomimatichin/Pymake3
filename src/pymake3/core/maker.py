"""
Provides the Maker class, which is a sort of target manager in pymake3. This
class is where all the targets are stored.
"""

#---------------------------------------
# IMPORTS
#---------------------------------------

from pymake3                 import report
from pymake3.core.exceptions import NoSuchTargetError
from pymake3.core.target     import Target

#---------------------------------------
# CLASSES
#---------------------------------------

class Maker(object):
    """
    Provides functionality for managing and making targets.
    """
    #---------------------------------------
    # STATIC ATTRIBUTES
    #---------------------------------------

    # The singleton instance.
    _inst = None

    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self):
        """
        Initializes a new instance of the Maker class.
        """
        self.def_target = None # Default target.
        self.targets    = []   # List with known targets.

    #---------------------------------------
    # METHODS
    #---------------------------------------

    def check_target(self, name, depends=()):
        """
        Checks a target's configuration for problems.

        :param name:    Name of the target to check.
        :param depends: Used internally to keep track of dependencies. Do not
                        specify.
        """
        if name in depends:
            report.error("target has circular dependency: '{}'", name)
            return

        depends += name,

        target = self.get_target(name, False)

        if not target:
            report.error("no such target: '{}'", name)
            return

        if not target.func:
            report.warn("unbound target: '{}'", name)

        if target.checked:
            return

        target.checked = True

        for depend in target.depends:
            self.check_target(depend, depends)

    def check_targets(self):
        """
        Checks all targets for problems.
        """
        for target in self.targets:
            self.check_target(target.name)

    def get_target(self, name, create=True):
        """
        Retrieves a target with the specified name. If no such target exists, it
        will be created if the 'create' parameter is set to 'True'. Otherwise,
        'None' will be returned.

        :param name:   Name of the target to retrieve.
        :param create: Whether to create a new target if one does not exist.
        """
        for target in self.targets:
            if target.name == name:
                return target

        if not create:
            return None

        target = Target(name)

        self.targets.append(target)

        return target

    def make(self, name, conf, completed=None):
        """
        Makes the target with the specified name.

        :param name: Name of the target to make.
        :param conf: Make configuration to use.
        """
        if completed is None:
            completed = []

        if name in completed:
            return

        target = self.get_target(name, False) if name else self.def_target

        if not target or not target.func:
            raise NoSuchTargetError(name)

        for depend in target.depends:
            self.make(depend, conf, completed)

        target.make(conf)
        completed.append(name)

    @staticmethod
    def inst():
        """
        Gets the Maker singleton instance.

        :return: The Maker singleton instance.
        """
        if not Maker._inst:
            Maker._inst = Maker()

        return Maker._inst

#---------------------------------------
# FUNCTIONS
#---------------------------------------

def make(target, conf):
    """
    Makes the target with the specified name.

    :param name: Name of the target to make.
    :param conf: Make configuration to use.
    """
    Maker.inst().make(target, conf)
