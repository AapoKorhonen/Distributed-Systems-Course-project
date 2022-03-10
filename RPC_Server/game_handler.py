import game


class GameHandler:

    def __init__(self, database):
        self.db = database
        self.player1 = None
        self.player2 = None

    def alusta_pelaajat(self, p1 =None, p2=None):
        if not self.player1:
            self.player1 = p1

        elif not self.player2:
            self.player2 = p2

        

    def create_db_object(self, p1, p2, outcome):
        #kutsuu databasea ja luo sinne uuden objektin
        #__gameID = self.db.----#1.luo database funktiolla uuden ID
        #self.db.-----(gameID, p1, p2, outcome) #luo uuden objektin
        pass

    