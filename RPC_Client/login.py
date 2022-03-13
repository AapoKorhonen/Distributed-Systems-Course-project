import socket
import time
###########################################
# LOGIN Class
# Käsittelee login toiminnot
# Tällä hetkellä ottaa yhteyttä serveriin
#   ja lähettää sinne sanan "login".
#
# Sen jälkeen pyytää käyttäjältä käyttäjänimen
#   ja lähettää sen serveriin.
#
# Lopuksi kuuntelee servetin vastausta ja
# tulostaa jos vastaus tulee.
# ###########################################

class Login:

    def __init__(self, hostname = '127.0.0.1', port = 8001):
        self.hostname = '127.0.0.1'
        self.port = 8001
        self.address = (hostname, port)
        self.FORMAT = 'utf-8'

    def main(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.connect(self.address)
            mes = "login"
            message = mes.encode(self.FORMAT)
            sock.send(message)
            print("Kirjaudutaan käyttäjä tilillesi:\n")

            username = input("Anna käyttäjänimi\n")
            message = username.encode(self.FORMAT)
            sock.send(message)
            password = input("Salasana\n")
            message = password.encode(self.FORMAT)
            sock.send(message)
            HEADER = 64
            name = sock.recv(HEADER).decode(self.FORMAT)
            while not name:
                name = sock.recv(HEADER).decode(self.FORMAT)
            # Receive data from server (i.e., current server time)
            print(name)
            if name == "KIRJAUTUMINEN ONNISTUI":
                return username, password
            return None, None
            print("JEE!")
        return 0