import sqlite3
import threading


class Database:
    
    
    def __init__(self ,filename):
    
        #self.conn = sqlite3.connect(filename)
        self.filename = filename
        self.id = 0
        self.make_tables()
        self._lock = threading.Lock()
        
        
        
    
    
    def make_tables(self):
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento1 = """create table USERS 
                        (USERNAME STRING PRIMARY KEY,PASSWORD STRING NOT NULL) """
            cursor.execute(komento1)
            komento2 = """create table GAMES (ID INT PRIMARY KEY, 
                        PLAYER1 STRING NOT NULL, PLAYER2 STRING NOT NULL, OUTCOME STRING) """
            cursor.execute(komento2)
            conn.commit()

        except:
            print("Taulukot jo olemassa")
            self.id = self.init_id()
            

    def init_id(self):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT ID FROM GAMES 
                        WHERE ID IS (SELECT MAX(ID) FROM GAMES)"""
            cursor.execute(komento)
            ID = int(cursor.fetchall())
            conn.commit()
            print("Onnistui")
        except:
            print("VIRHE init_id")
            ID = 0
        
        return ID
     
    def get_ID(self):
    
        with self._lock:
            ID = self.id
            self.id = self.id + 1
            
        return ID

     
    def insert_new_user(self, username, password):

        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            datat = (username, password)
            
            komento = """INSERT INTO USERS
                              (username, password) 
                              VALUES (?, ?);"""
            cursor.execute(komento, datat)
            conn.commit()
        except:
            print("VIRHE insert_new_user")
            return 1
    
        return 0
        
    
    def insert_game_history(self, ID , p1, p2, outcome):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            datat = (ID, p1, p2, outcome)
            
            komento = """INSERT INTO GAMES
                              (ID, PLAYER1, PLAYER2, OUTCOME) 
                              VALUES (?, ?, ?, ? );"""
            cursor.execute(komento, datat)
            conn.commit()
        except:
            print("VIRHE INSERT_GAME_HISTORY")
            return 1
        return 0
        
    
    def get_user_information(self):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT * FROM USERS;"""
            cursor.execute(komento)
            ID = cursor.fetchall()
            conn.commit()
        except:
            print("ERROR")
        
        
        return ID
    
    
    def get_game_information(self):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT * FROM GAMES;"""
            cursor.execute(komento)
            ID = cursor.fetchall()
            conn.commit()
        except:    
            print("ERROR")
            return 0
        return ID
        
    def get_game_info_user(self):
        return 0
    
    def get_game_info_wins_user(self, username):
    
        try:
            conn = sqlite3.connect(self.filename)
            cursor =conn.cursor()
            komento = """SELECT COUNT(OUTCOME) FROM GAMES WHERE OUTCOME = ?;"""
            cursor.execute(komento, (username,))
            ID = int(cursor.fetchall()[0][0])
            conn.commit()
        except:    
            print("ERROR")
            return 0
        return ID
        
        
    def check_credentials(self, username, password):
    
        arvo = False
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT PASSWORD FROM USERS WHERE USERNAME = ?;"""
            cursor.execute(komento, (username, ))
            password_test = cursor.fetchall()
            conn.commit()
            print(password_test[0][0])
            if password == password_test[0][0]:
            
                arvo = True
            
        except:   
            print("ERROR check_credentials")
            
        
        return arvo
        
        
        