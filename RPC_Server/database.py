import sqlite3
import threading


class Database:
    
    
    def __init__(self ,filename):
    
        self.conn = sqlite3.connect(filename)
        self.id = 0
        self.make_tables()
        self._lock = threading.Lock()
        
        
        
    
    
    def make_tables(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("create table USERS (USER STRING PRIMARY KEY,PASSWORD STRING NOT NULL) " )
            cursor.execute("create table GAMES (ID INT PRIMARY KEY, PLAYER1 STRING NOT NULL, PLAYER2 STRING NOT NULL, OUTCOME STRING) " )
            self.conn.commit()

        except:
            print("Taulukost jo olemassa")
            self.id = self.init_id()
            

    def init_id(self):
        
        try:
            cursor = self.connect.cursor()
            cursor.execute("SELECT ID FROM GAMES WHERE ID IS (SELECT MAX(ID) FROM GAMES)")
            ID = int(cursor.fetchall())
            print("Onnistui")
        except:
            print("ERRORi")
            ID = 0
        
        return ID
     
    def get_ID(self):
    
        with self._lock:
            ID = self.id
            self.id = self.id + 1
            
        return ID

     
    def insert_new_user(self, username, password):
    
        cursor = self.conn.cursor()
        
    
    
        return 0
        
    
    def insert_game_history(self, ID , p1, p2, outcome):
        return 0
        
    
    def get_user_information():
        return 0
        
    
    def get_game_information():
        return 0
        
    def get_game_info_user():
        return 0
    
    def get_game_info_wins_user():
        return 0
        
        
        