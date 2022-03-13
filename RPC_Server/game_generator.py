import game_log
import game_handler
import error_handler
import time
import game

class GameGenerator:

    def __init__(self, database):
        self._error = error_handler.ErrorHandler()
        self._gameslist = []
        self._database = database

    def _free_games(self):
        #list of free games, odotus lista
        try:
            if len(self._gameslist) == 0:
                return 0, 0, 0
            else:
                peli = self._gameslist.pop(-1)
                return peli

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameGenerator._free_games method!"
            self._error.print_error(e, respond_body)


    
    def main_(self, p1, opponent = 0):

        if opponent == 0:

            time.sleep(1)

            p1.send_message("Peli tekoälyä vastaan\n")

            game1 = game.Game(p1.get_username(), "AI")

            gamehandler = game_handler.GameHandler(self._database, p1, 0, game1)
            time.sleep(1)

            p1.send_message("Liitetään peliin\n")

            time.sleep(1)

            gamehandler.main_()

            return game1
        elif opponent == 1:
            pelihandler, p2, game2 = self._free_games()
            if pelihandler == 0:
                p1.send_message("Vapaita pelejä ei löytynyt, odotetaan vastustajaa \n")
                game1 = game.Game(p1.get_username(), None)
                self._gameslist.append([game_handler.GameHandler(self._database, p1, 1, game1), p1, game1])
                return game1
            else:
                time.sleep(1)
                p1.send_message("Vapaa peli löytyi, yhdistetään...\n")
                p2.send_message("Vastustaja on löytynyt\n"
                                "Pelaat käyttäjää " + p1.get_username() + " vastaan\n")
                pelihandler.initialize_players(None, p1)
                time.sleep(1)
                game2.insert_p2(p1.get_username())
                p1.send_message("Pelaat käyttäjää " + p2.get_username() + " vastaan\n")
                time.sleep(1)
                pelihandler.main_()
                return game2
            #gamehandler = game_handler.GameHandler(self._database, p1, 1)

