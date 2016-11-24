#---------------------------------------
# CLASSES
#---------------------------------------

class NoSuchTargetError(Exception):
    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self, target_name):
        super(NoSuchTargetError, self).__init__("no such target")

        self.target_name = target_name
