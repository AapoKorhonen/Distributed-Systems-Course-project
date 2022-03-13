import sqlite3
import threading
import error_handler


class Database:
    
    
    def __init__(self ,filename):
    
        #self.conn = sqlite3.connect(filename)
        self.filename = filename
        self.id = 0
        self._lock = threading.Lock()
        self._error = error_handler.ErrorHandler()
        self._make_tables()
        
        
    
    
    def _make_tables(self):
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

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._make_tables method!"
            self._error.print_error(e, respond_body)
            print("Tables already exist!")
            self.id = self._init_id()

    def _init_id(self):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT ID FROM GAMES 
                        WHERE ID IS (SELECT MAX(ID) FROM GAMES)"""
            cursor.execute(komento)
            ID = cursor.fetchall()
            ID = int(ID[0][0]) + 1
            conn.commit()

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._init_id method!"
            self._error.print_error(e, respond_body)
            ID = 0
        
        return ID
     
    def get_ID(self):
        
        try:
            with self._lock:
                ID = self.id
                self.id = self.id + 1
        
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._get_ID method!"
            self._error.print_error(e, respond_body)
            print("Error init_id")
            ID = 0
            
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
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._insert_new_user method!"
            self._error.print_error(e, respond_body)
            conn.commit()
            return 1    
        return 0
        
    
    def _insert_game_history(self, ID , p1, p2, outcome):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            datat = (ID, p1, p2, outcome)
            komento = """INSERT INTO GAMES
                              (ID, PLAYER1, PLAYER2, OUTCOME) 
                              VALUES (?, ?, ?, ? );"""
            cursor.execute(komento, datat)

            conn.commit()
        
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._insert_game_history method!"
            self._error.print_error(e, respond_body)
            conn.commit()
            return 1
        return 0
        
    
    def _get_user_information(self):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT * FROM USERS;"""
            cursor.execute(komento)
            ID = cursor.fetchall()

            conn.commit()
        
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._get_user_information method!"
            self._error.print_error(e, respond_body)
            conn.commit()
            return 0
        
        return ID
    
    
    def _get_game_information(self):
        
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT * FROM GAMES;"""
            cursor.execute(komento)
            ID = cursor.fetchall()

            conn.commit()
        
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._get_game_information method!"
            self._error.print_error(e, respond_body)
            conn.commit()
            return 0

        
        return ID
        
    def _get_game_info_user(self):
        try:
            return 0

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._get_game_info_user method!"
            self._error.print_error(e, respond_body)
        
    
    def _get_game_info_wins_user(self, username):
    
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT COUNT(OUTCOME) FROM GAMES WHERE OUTCOME = ?;"""
            cursor.execute(komento, (username,))
            wins = int(cursor.fetchall()[0][0])

            conn.commit()

            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT COUNT(OUTCOME) FROM GAMES WHERE PLAYER1 = ? OR PLAYER2 = ?;"""
            cursor.execute(komento, (username, username))
            games = int(cursor.fetchall()[0][0])

            conn.commit()
        
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._get_game_info_wins_user method!"
            self._error.print_error(e, respond_body)
            return 0

        return wins, games
        
        
    def _check_credentials(self, username, password):
    
        arvo = False
        try:
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            komento = """SELECT PASSWORD FROM USERS WHERE USERNAME = ?;"""
            cursor.execute(komento, (username, ))
            password_test = cursor.fetchall()
            conn.commit()
            if len(password_test) == 0:
                arvo = False
            elif password == password_test[0][0]:
                arvo = True

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in Database._check_credentials method! \
                            \nERROR: check_credentials!"
            self._error.print_error(e, respond_body)   
            
        
        return arvo
        
        
        