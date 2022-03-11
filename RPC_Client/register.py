import socket

###########################################
# REGISTER Class
# Käsittelee register toiminnot
# Tällä hetkellä vain ottaa yhteyttä serveriin
#   ja lähettää sinne sanan "register".
#
# ###########################################

class Register:

    def __init__(self, hostname='127.0.0.1', port=8001):
        self.hostname = '127.0.0.1'
        self.port = 8001
        self.address = (hostname, port)
        self.FORMAT = 'utf-8'

    def main(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.connect(self.address)
            mes = "register"
            message = mes.encode(self.FORMAT)
            sock.send(message)
            # Receive data from server (i.e., current server time)
            print("JEE!")
        return 0