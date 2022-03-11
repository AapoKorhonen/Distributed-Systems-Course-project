"""
This is Rock-Paper-Scissors server.

https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
"""


import datetime
import socket
import ssl
import error_handler
import user
import database
import communication_handler
import game_generator
import threading
import log


class RPCServer:
    def __init__(self, pem, key):
        self._database = None
        self._pem = pem
        self._key = key
        self._error = error_handler.ErrorHandler()
        self.log_system = log.Log()



    def _handle_game(self, connection, address):
        ##########################
        # Käsittelee game pyynnöt
        #  (Voi ajatella /game )
        # Nyt vain tulostaa "_handle_game"
        #
        # Jatkossa tässä siirretään käyttäjä
        # game_generaattoriin ja siitä eteenpäin
        ##########################
        print("_handle_game")
        return 0

    def _handle_register(self, connection, address):
        ##########################
        # Käsittelee register pyynnöt
        #  (Voi ajatella /register )
        # Nyt vain tulostaa "_handle_register"
        #
        # Jatkossa tässä registöröidään käyttäjä (mahdollisesti omassa oliossa ?)
        ##########################
        print("_handle_register")
        return 0

    def _handle_login(self,connection, address):
        ##########################
        # Käsittelee login pyynnöt
        #  (Voi ajatella /login )
        # Testi mielessä olen tähän tehnyt eniten ominaisuuksia
        # Nyt jää aluksi kuuntelemaan clientin seuraavaa viestiä, eli käyttäjänimeä (while not true name)
        # Sitten luo uuden User- olion
        # Lopuksi User olion send_message metodilla lähettää viestin clientille, että "käyttäjä luotu" TESTATKAA ETTÄ TOIMII
        # Jatkossa tässä siirretään käyttäjä
        # game_generaattoriin ja siitä eteenpäin
        ##########################
        HEADER = 64
        FORMAT = 'utf-8'
        print("_handle_login")
        name = connection.recv(HEADER).decode(FORMAT)
        while not name:
            name = connection.recv(HEADER).decode(FORMAT)
        print(name)

        user1 = user.User(name, connection, address)
        user1.send_message("käyttäjä luotu")
        print("kaka")


        return 0

    def _handle_stats(self, connection, address):
        ##########################
        # Käsittelee stats pyynnöt
        #  (Voi ajatella /stats )
        # Nyt vain tulostaa "_handle_stats"
        #
        # Lopullisessa versiossa tässä mahdollisesti vaan etitään databasesta käyttäjän pelit ja lähetetään ne clientille
        ##########################
        print("_handle_stats")
        return 0

    def _handle_thread(self, connection, address):

        ##########################
        # Käsittelee ensimmäisenä yhteyden
        # Tarkistaa mikä on ensimmäinen clientin lähettämä
        # viesti.
        #
        # Mahdolliset clientin lähettämä viesti ovat:
        #   register
        #   login
        #   game
        #   stats
        ##########################

        HEADER = 64
        FORMAT = 'utf-8'
        message = connection.recv(HEADER).decode(FORMAT)
        print(message)
        if message == "register":
            self._handle_register(connection, address)
        elif message == "login":
            self._handle_login(connection, address)
        elif message == "game":
            self._handle_game(connection, address)
        elif message == "stats":
            self._handle_stats(connection, address)
        else:
            print("ONGELMA")

        connection.close()

    def _create_socket(self): # leading '_' in the method name distinguishes 
                                # private and public methods
        try:
            hostname = '127.0.0.1' # loopback address

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
                sock.bind((hostname, 8001))
                sock.listen(5)
                while True:
                    # Keep accepting connections from clients
                    conn, addr = sock.accept()
                    thread = threading.Thread(target=self._handle_thread, args=(conn,addr))
                    thread.start()
        except OSError as e:
            respond_body = "OSError in _create_socket method!"
            self._error.print_error(e, respond_body)
        except Exception as e:
            respond_body = "Error in _create_socket method!"
            self._error.print_error(e, respond_body)
    


    def _create_database(self):
        try:
            self._database = database.Database("database.db")
        except Exception as e:
            respond_body = "Error in _create_database method!"
            self._error.print_error(e, respond_body)



    def _main(self): 
        """This method calls all the necessary classes to 
        run the server."""
        server = RPCServer(self._pem, self._key)
        self.log_system.log("Initializing database...")
        server._create_database()
        # you need to initialize other handlers before opening the socket connection
        self.log_system.log("Creating game generator...")

        self.log_system.log("Creating socket connection...")
        server._create_socket()
       
        


if __name__ == '__main__':
    """Server can be run only directly calling the 
    RPC_Server class."""

    # get certification file and private key
    pem = 'Certificates/server.pem'
    key = 'Certificates/server.key'

    # create server instance
    server = RPCServer(pem, key)

    # start server
    server._main()










