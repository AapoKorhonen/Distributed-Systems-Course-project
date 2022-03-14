"""This class creates the game handler class. It sends the game messages to the client through
communication handler, receives the game moves from players and plays them using the Game-class."""

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
        """This method returns the game list."""
        try:
            if len(self._gameslist) == 0:
                return 0, 0, 0
            else:
                peli = self._gameslist.pop(-1)
                return peli

        except Exception as e:
            respond_body = "Error in GameGenerator._free_games method!"
            self._error.print_error(e, respond_body)

    def main_(self, p1, opponent=0):
        """This main method connects the two players to the same game and messages players when
        the game has been found."""
        if opponent == 0:

            time.sleep(1)

            p1.send_message("Game against AI.\n")

            game1 = game.Game(p1.get_username(), "AI")

            gamehandler = game_handler.GameHandler(
                self._database, p1, 0, game1)
            time.sleep(1)

            p1.send_message("Joining the game...\n")

            time.sleep(1)

            gamehandler.main_()

            return game1
        elif opponent == 1:
            handler, p2, game2 = self._free_games()
            if handler == 0:
                p1.send_message(
                    "No free games available, waiting for opponent. \n")
                game1 = game.Game(p1.get_username(), None)
                self._gameslist.append([game_handler.GameHandler(
                    self._database, p1, 1, game1), p1, game1])
                return game1
            else:
                time.sleep(1)
                p1.send_message("Game found! Connecting...\n")
                p2.send_message("Opponent found\n"
                                "You are playing against " + p1.get_username() + " \n")
                handler.initialize_players(None, p1)
                time.sleep(1)
                game2.insert_p2(p1.get_username())
                p1.send_message("You are playing against " +
                                p2.get_username() + " \n")
                time.sleep(1)
                handler.main_()
                return game2
