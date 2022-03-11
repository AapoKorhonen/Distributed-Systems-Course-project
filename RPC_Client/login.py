import socket

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
            masneg = input("Anna käyttäjänimi")
            messag = masneg.encode(self.FORMAT)
            sock.send(messag)
            HEADER = 64
            FORMAT = 'utf-8'
            name = sock.recv(HEADER).decode(FORMAT)
            while not name:
                name = sock.recv(HEADER).decode(FORMAT)
            # Receive data from server (i.e., current server time)
            print(name)
            print("JEE!")
        return 0