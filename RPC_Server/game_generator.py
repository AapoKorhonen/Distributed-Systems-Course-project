import game_log
import game_handler
import error_handler


class GameGenerator:

    def __init__(self):
        self._error = error_handler.ErrorHandler()

    def _create_gameHandler(self):
       #creates the game_handler by using the class
        try:
            pass

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameGenerator._create_gameHandler method!"
            self._error.print_error(e, respond_body)

    def _create_log(self):
        #creates log for the game
        try:
            pass

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameGenerator._create_log method!"
            self._error.print_error(e, respond_body)

    def _attach_user_to_game(self):
        #Yhdistää create gameHandlerin, login ja pelaajan
        try:
            pass

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameGenerator._attach_user_to_game method!"
            self._error.print_error(e, respond_body)

    def _create_gameID(self):
        #create gameID
        try:
            pass

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameGenerator._create_gameID method!"
            self._error.print_error(e, respond_body)

    def _free_games(self, lista):
        #list of free games, odotus lista
        try:
            print(lista)
            pass

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameGenerator._free_games method!"
            self._error.print_error(e, respond_body)


    
