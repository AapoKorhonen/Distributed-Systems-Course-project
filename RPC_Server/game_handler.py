from distutils.log import error
import game
import error_handler

class GameHandler:

    def __init__(self, database):
        self._db = database
        self._player1 = None
        self._player2 = None
        self._error = error_handler.ErrorHandler()

    def _initialize_players(self, p1 =None, p2=None):
        try:
            if not self._player1:
                self._player1 = p1

            elif not self._player2:
                self._player2 = p2

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameHandler._initialize_players method!"
            self._error.print_error(e, respond_body)

        

    def _create_db_object(self, p1, p2, outcome):
        #kutsuu databasea ja luo sinne uuden objektin
        #__gameID = self.db.----#1.luo database funktiolla uuden ID
        #self.db.-----(gameID, p1, p2, outcome) #luo uuden objektin
        try:
            pass

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameHandler._create_db_object method!"
            self._error.print_error(e, respond_body)

    