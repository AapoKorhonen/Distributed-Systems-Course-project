"""This is a Log-class. It handles all the necessary log messages. It is the same class 
in the server side and the client side."""

class Log:

    def __init__(self):

        """ ANSI color codes """
        self.BLACK = "\033[0;30m"
        self.RED = "\033[0;31m"
        self.GREEN = "\033[0;32m"
        self.BROWN = "\033[0;33m"
        self.BLUE = "\033[0;34m"
        self.PURPLE = "\033[0;35m"
        self.CYAN = "\033[0;36m"
        self.LIGHT_GRAY = "\033[0;37m"
        self.DARK_GRAY = "\033[1;30m"
        self.LIGHT_RED = "\033[1;31m"
        self.LIGHT_GREEN = "\033[1;32m"
        self.YELLOW = "\033[1;33m"
        self.LIGHT_BLUE = "\033[1;34m"
        self.LIGHT_PURPLE = "\033[1;35m"
        self.LIGHT_CYAN = "\033[1;36m"
        self.LIGHT_WHITE = "\033[1;37m"
        self.BOLD = "\033[1m"
        self.FAINT = "\033[2m"
        self.ITALIC = "\033[3m"
        self.UNDERLINE = "\033[4m"
        self.BLINK = "\033[5m"
        self.NEGATIVE = "\033[7m"
        self.CROSSED = "\033[9m"
        self.END = "\033[0m"

    def log(self, message, error=False):

        if error:
            print(self.RED + message)
        else:
            print(self.GREEN + message)

        return 0

