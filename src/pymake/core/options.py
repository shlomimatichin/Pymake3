#---------------------------------------
# CLASSES
#---------------------------------------

class Options(object):
    def __init__(self):
        self.no_color = False
        self.no_exit  = False
        self.no_warn  = False

    def parse(self, opt):
        if opt.find('=') > 0:
            s     = opt.split('=', 1)
            opt   = s[0]
            value = s[1]

        if opt == '--no-color':
            self.no_color = True
            return True

        if opt == '--no-exit':
            self.no_exit = True
            return True

        if opt == '--no-warn':
            self.no_warn = True
            return True

        return False
