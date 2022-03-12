"""
This creates connection for the client.
"""

import socket
import login
import stats
import register
import play
import ssl

class Client:
    def __init__(self, client_pem, hostname, port):

        ###########################################
        # Valmistellaan client
        # Alustetaan login, stats, register, play oliot
        ###########################################

        self._client_pem = client_pem
        self.login = login.Login(hostname, port)
        self.stats = stats.Stats(hostname, port)
        self.register = register.Register(hostname, port)
        self.play = play.Play(hostname, port)
    

    def _main(self):
        ###########################################
        # Kerrotaan käyttäjälle mitä vaihtoehtoja on
        # Luetaan käyttäjän syöte ja "käynnistetään"
        # sitä toimintoa vastaava olio.
        ###########################################
        print("Valitse:\n"
              "login\n"
              "register\n"
              "stats\n"
              "play\n")
        while True:
            valinta = input()
            if valinta == "login":
                self.login.main()
            elif valinta == "register":
                self.register.main()
            elif valinta == "stats":
                self.stats.main()
            elif valinta == "play":
                self.play.main()
            

if __name__ == '__main__':
    pem = 'Certificates/server.pem'
    client = Client(pem, '127.0.0.1', 8001)
    client._main()