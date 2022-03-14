"""
This creates connection for the client.
"""

import login
import stats
import register
import play
import exit_client
import error_handler


class Client:
    def __init__(self, client_pem, hostname, port):
        """Initialize class methods login, stats, register and game instances."""

        self._client_pem = client_pem
        self.login = login.Login(hostname, port)
        self.stats = stats.Stats(hostname, port)
        self.register = register.Register(hostname, port)
        self.play = play.Play(hostname, port)
        self.exit = exit_client.ExitClient(hostname, port)
        self._error = error_handler.ErrorHandler()
        self._username = None
        self._password = None

    def _main(self):
        """This main method tells to the user which input choises it has and creates instances."""

        try:
            connected = True
            print("Main menu:\n"
                  "login\n"
                  "register\n"
                  "stats\n"
                  "play\n"
                  "exit\n")
            while connected:
                valinta = input()
                if valinta == "login":
                    self._username, self._password = self.login.main()
                elif valinta == "register":
                    self.register.main()
                elif valinta == "stats":
                    if self._username == None:
                        print("Login first!\n")
                    else:
                        self.stats.main(self._username, self._password)
                elif valinta == "play":
                    if self._username == None:
                        print("Login first!\n")
                    else:
                        self.play.main(self._username, self._password)
                elif valinta == "exit":
                    self.exit.main()
                    connected = False

                print("\nMain menu:\n"
                      "login\n"
                      "register\n"
                      "stats\n"
                      "play\n"
                      "exit\n")

        except Exception as e:
            respond_body = "Error in Client._main method!"
            self._error.print_error(e, respond_body)


if __name__ == '__main__':
    pem = 'Certificates/server.pem'
    client = Client(pem, '127.0.0.1', 8001)
    client._main()
