"""
Contains the exception and error classes.
"""

#---------------------------------------
# CLASSES
#---------------------------------------

class NoSuchTargetError(Exception):
    """
    An attempt was made to make a target that does not exist.
    """
    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self, target_name):
        """
        Initializes the exception.

        :param target_name: Name of the missing target.
        """
        super(NoSuchTargetError, self).__init__("no such target")

        self.target_name = target_name
