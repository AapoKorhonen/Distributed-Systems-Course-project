"""
This is Rock-Paper-Scissors server class.
"""

import socket
import error_handler
import user
import database
import game_generator
import threading
import log
import authentication_handler
import time


class RPCServer:
    def __init__(self, pem, key):
        self._database = None
        self._pem = pem
        self._key = key
        self._error = error_handler.ErrorHandler()
        self.log_system = log.Log()
        self._database = database.Database("database.db")
        self._authentication = authentication_handler.AuthenticationHandler(
            self._database)
        self._game_generator = game_generator.GameGenerator(self._database)

        self.HEADER = 64
        self.FORMAT = 'utf-8'

    def _handle_game(self, connection, address):
        """This method handles the creation of /game URL context. It checks if user is logged in
        and forwards the user to the game generator."""

        try:
            self.log_system.log("_handle_game")
            name = connection.recv(self.HEADER).decode(self.FORMAT)
            while not name:
                name = connection.recv(self.HEADER).decode(self.FORMAT)
            salasana = connection.recv(self.HEADER).decode(self.FORMAT)
            while not salasana:
                salasana = connection.recv(self.HEADER).decode(self.FORMAT)

            if self._authentication.check_authentication(name, salasana):
                user1 = user.User(name, connection, address)
                opponent = connection.recv(self.HEADER).decode(self.FORMAT)
                while not opponent:
                    opponent = connection.recv(self.HEADER).decode(self.FORMAT)
                if opponent == "0":
                    game = self._game_generator.main_(user1, 0)
                elif opponent == "1":
                    game = self._game_generator.main_(user1, 1)

                while not game.game_finished():
                    time.sleep(1)

        except Exception as e:
            respond_body = "Error in _handle_game method!"
            self._error.print_error(e, respond_body)
        return 0

    def _handle_register(self, connection, address):
        """This method handles the creation of /register URL context. The user sends their
        username and password and they are inserted to the database. The user must register
        before playing or retrieving stats from the database."""

        try:
            HEADER = 64
            FORMAT = 'utf-8'
            self.log_system.log("_handle_register")
            name = connection.recv(HEADER).decode(FORMAT)
            while not name:
                name = connection.recv(HEADER).decode(FORMAT)
            salasana = connection.recv(HEADER).decode(FORMAT)
            while not salasana:
                salasana = connection.recv(HEADER).decode(FORMAT)
            if self._database.insert_new_user(name, salasana) == 0:
                connection.send("Registration succeeded!\n".encode(FORMAT))
            else:
                connection.send("Registration failed!\n".encode(FORMAT))

        except Exception as e:
            respond_body = "Error in _handle_register method!"
            self._error.print_error(e, respond_body)

        return 0

    def _handle_login(self, connection, address):
        """This method handles the creation of /login URL context. It checks if the user is
        registered and if so, it creates new User-class."""

        try:
            HEADER = 64
            FORMAT = 'utf-8'
            self.log_system.log("_handle_login")
            name = connection.recv(HEADER).decode(FORMAT)
            while not name:
                name = connection.recv(HEADER).decode(FORMAT)
            salasana = connection.recv(HEADER).decode(FORMAT)
            while not salasana:
                salasana = connection.recv(HEADER).decode(FORMAT)
            if self._authentication.check_authentication(name, salasana):
                user1 = user.User(name, connection, address)
                user1.send_message("Login succeeded!")
            else:
                user1 = user.User(name, connection, address)

                user1.send_message("Error in Login!")
                self.log_system.log("Error in Login!")

        except Exception as e:
            respond_body = "Error in _handle_login method!"
            self._error.print_error(e, respond_body)

        return 0

    def _handle_stats(self, connection, address):
        """This method handles the 'stats' URL context creation. It returns amount of wins
        and played games to the user."""

        try:
            HEADER = 64
            FORMAT = 'utf-8'
            self.log_system.log("_handle_stats")
            name = connection.recv(HEADER).decode(FORMAT)
            while not name:
                name = connection.recv(HEADER).decode(FORMAT)
            salasana = connection.recv(HEADER).decode(FORMAT)
            while not salasana:
                salasana = connection.recv(HEADER).decode(FORMAT)
            if self._authentication.check_authentication(name, salasana):
                user1 = user.User(name, connection, address)
                wins, games = self._database._get_wins_user(name)
                user1.send_message("Wins: " + str(wins) +
                                   "\nGames: " + str(games) + "\n")

        except Exception as e:
            respond_body = "Error in _handle_stats method!"
            self._error.print_error(e, respond_body)

        return 0

    def _handle_thread(self, connection, address):
        """This method handles threading of the multiple simultaneous client connections."""

        try:
            HEADER = 64
            FORMAT = 'utf-8'
            connected = True
            while connected:
                message = connection.recv(HEADER).decode(FORMAT)
                while not message:
                    message = connection.recv(HEADER).decode(FORMAT)
                self.log_system.log(message)
                if message == "register":
                    self._handle_register(connection, address)
                elif message == "login":
                    self._handle_login(connection, address)
                elif message == "game":
                    self._handle_game(connection, address)
                elif message == "stats":
                    self._handle_stats(connection, address)
                elif message == "exit":
                    connected = False
                    self.log_system.log(f"Exit operated for client {address}")
                else:
                    self.log_system.log("PROBLEM: Wrong context name!")

            connection.close()
            self.log_system.log(f"Connection closed: {address}")

        except Exception as e:
            respond_body = "Error in _handle_thread method!"
            self._error.print_error(e, respond_body)

    def _create_socket(self):
        """This method creates socket connections for the clients and gives the connection to
        the thread handling method."""

        try:
            hostname = '0.0.0.0'
            # hostname = '127.0.0.1' # loopback address

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
                sock.bind((hostname, 8001))
                sock.listen(5)
                while True:
                    # Keep accepting connections from clients
                    conn, addr = sock.accept()
                    thread = threading.Thread(
                        target=self._handle_thread, args=(conn, addr))
                    thread.start()
        except OSError as e:
            respond_body = "OSError in _create_socket method!"
            self._error.print_error(e, respond_body)
        except Exception as e:
            respond_body = "Error in _create_socket method!"
            self._error.print_error(e, respond_body)

    def _main(self):
        """This method calls all the necessary classes to 
        run the server."""
        try:
            server = RPCServer(self._pem, self._key)
            self.log_system.log("Initializing database...")
            self.log_system.log("Creating socket connection...")
            server._create_socket()

        except Exception as e:
            respond_body = "Error in _main method!"
            self._error.print_error(e, respond_body)


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
