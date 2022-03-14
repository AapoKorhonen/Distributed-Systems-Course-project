"""This class handles the client login."""

import socket


class Login:

    def __init__(self, hostname='127.0.0.1', port=8001):
        self.hostname = '127.0.0.1'
        self.port = 8001
        self.address = (hostname, port)
        self.FORMAT = 'utf-8'

    def main(self):
        """This method handles the client login to the server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.connect(self.address)
            mes = "login"
            message = mes.encode(self.FORMAT)
            sock.send(message)
            print("Registering to your user account.:\n")

            username = input("Give username:\n")
            message = username.encode(self.FORMAT)
            sock.send(message)
            password = input("Give password:\n")
            message = password.encode(self.FORMAT)
            sock.send(message)
            HEADER = 64
            name = sock.recv(HEADER).decode(self.FORMAT)
            while not name:
                name = sock.recv(HEADER).decode(self.FORMAT)
            print(name)
            if name == "Registration succeeded!":
                return username, password
            return None, None
        return 0
