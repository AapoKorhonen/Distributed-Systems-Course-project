from distutils.log import error
import game
import error_handler
import game
import time
import game_log
class GameHandler:

    def __init__(self, database, p1, opponent, game):
        # OPPONENT = 0   : game against AI
        # OPPONENT = 1   : game against another player
        self._database = database
        self._player1 = p1
        self._player2 = None
        self._error = error_handler.ErrorHandler()
        self._game = game
        self._opponent = opponent
        self._gameID = self._database.get_ID()
        self.winner = None
        self._log = game_log.GameLog("gamelog.txt")

    def initialize_players(self, p1 =None, p2=None):
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
        try:
            self._database._insert_game_history(self._gameID, p1, p2, outcome)

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameHandler._create_db_object method!"
            self._error.print_error(e, respond_body)


    def main_(self):
        try:
            if self._opponent == 0:

                self._player1.send_message("Peli alkaa, anna liikkeesi\n")
                move = self._player1.recieve_message()
                move1 = self._game.p1_move(move)
                move2 = self._game.ai_p2_move()
                self._player1.send_message(move2)
                self.winner = self._game.solve_game()
                self._log.write_gamelog(self._player1.get_username() + ": " + move1 + ", AI: " + move2 + ", Winner: " + self.winner + "\n")
                
                time.sleep(3)

                if self.winner == self._player1.get_username():
                    self._player1.send_message("Voitit pelin\n")
                elif self.winner == "Tie":
                    self._player1.send_message("Tasapeli\n")
                else:
                    self._player1.send_message("Hävisit pelin\n")
                self._create_db_object(self._player1.get_username(), "AI", self.winner)
            elif self._opponent == 1:

                self._player1.send_message("Peli alkaa, anna liikkeesi\n")
                self._player2.send_message("Peli alkaa, anna liikkeesi\n")

                move1 = self._player1.recieve_message()
                move2 = self._player2.recieve_message()

                move1 = self._game.p1_move(move1)
                move2 = self._game.p2_move(move2)

                self._player1.send_message(move2)
                self._player2.send_message(move1)

                self.winner = self._game.solve_game()
                self._log.write_gamelog(self._player1.get_username() + ": " + move1 + ", "+
                     self._player2.get_username() +" : " + move2 + 
                     ", Winner: " + self.winner + "\n")
                time.sleep(3)

                if self.winner == self._player1.get_username():
                    self._player1.send_message("Voitit pelin\n")
                    self._player2.send_message("Hävisit pelin\n")
                elif self.winner == "Tie":
                    self._player1.send_message("Tasapeli\n")
                    self._player2.send_message("Tasapeli\n")
                else:
                    self._player1.send_message("Hävisit pelin\n")
                    self._player2.send_message("Voitit pelin\n")

                self._create_db_object(self._player1.get_username(), self._player2.get_username(), self.winner)

        except Exception as e:
            respond_body = "Error in GameHandler._main_ method!"
            self._error.print_error(e, respond_body)
