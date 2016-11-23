#---------------------------------------
# CLASSES
#---------------------------------------

class Settings(object):
    def __init__(self):
        self.disable_colors   = False
        self.disable_warnings = False

    def parse(self, opt):
        if opt.find('=') > 0:
            s     = opt.split('=', 1)
            opt   = s[0]
            value = s[1]

        if opt == '--no-color':
            self.disable_colors = True
            return True

        if opt == '--no-warn':
            self.disable_warnings = True
            return True

        return False
