
class Game:

    def __init__(self, p1, p2):
        
        self.p1 = p1
        self.p2 = p2
        self.p1move = None
        self.p2move = None
        self.outcome = None
        
    
    def p1_move(self, move):
        self.p1move = move
    
    def p2_move(self, move):
        self.p2move = move

    def solve_game(self, ):
        
        if self.p1move == "R":
            if self.p2move == "R":
                self.outcome = "Tie"
            elif self.p2move == "P":
                self.outcome = self.p2
            elif self.p2move == "S":
                self.outcome = self.p1
                        
        elif self.p1move == "P":
                
            if self.p2move == "R":
                self.outcome = self.p1
            elif self.p2move == "P":
                self.outcome = "Tie"
            elif self.p2move == "S":
                self.outcome = self.p2

        elif self.p1move == "S":
        
            if self.p2move == "R":
                self.outcome = self.p2
            elif self.p2move == "P":
                self.outcome = self.p1
            elif self.p2move == "S":
                self.outcome = "Tie"

        
        return self.outcome

