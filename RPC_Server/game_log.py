import error_handler

class GameLog:

    def __init__(self, gamelogfile):
        self._error = error_handler.ErrorHandler()
        self.filename = gamelogfile

    def write_gamelog(self, event):
        ##################
        # Write_gamelog:
        # Takes event happening in the game and 
        # writing that down to the the log file
        #################

        try:
            f = open(self.filename, "a")
            f.write(event)
            f.close()

            f = open(self.filename, "r")
            print(f.read())
        except Exception as e:
            respond_body = "Error in write_gamelog!"
            self._error.print_error(e, respond_body)
        
