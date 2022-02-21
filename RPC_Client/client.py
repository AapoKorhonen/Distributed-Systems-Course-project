"""
This creates connection for the client.
"""

from pydoc import cli
import socket
import ssl

class Client:
    def __init__(self, client_pem):
        self._client_pem = client_pem
    
    def log(self, message, error=False):
            """ ANSI color codes """
            BLACK = "\033[0;30m"
            RED = "\033[0;31m"
            GREEN = "\033[0;32m"
            BROWN = "\033[0;33m"
            BLUE = "\033[0;34m"
            PURPLE = "\033[0;35m"
            CYAN = "\033[0;36m"
            LIGHT_GRAY = "\033[0;37m"
            DARK_GRAY = "\033[1;30m"
            LIGHT_RED = "\033[1;31m"
            LIGHT_GREEN = "\033[1;32m"
            YELLOW = "\033[1;33m"
            LIGHT_BLUE = "\033[1;34m"
            LIGHT_PURPLE = "\033[1;35m"
            LIGHT_CYAN = "\033[1;36m"
            LIGHT_WHITE = "\033[1;37m"
            BOLD = "\033[1m"
            FAINT = "\033[2m"
            ITALIC = "\033[3m"
            UNDERLINE = "\033[4m"
            BLINK = "\033[5m"
            NEGATIVE = "\033[7m"
            CROSSED = "\033[9m"
            END = "\033[0m"

            if error:
                print(RED + message)
            else:
                print(GREEN + message)

    def _main(self):
        try:
            client = Client(self._client_pem)
            hostname = '127.0.0.1'
            port = 8001
            address = (hostname, port)
            # PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.load_verify_locations(self._client_pem)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    print(ssock.version())
                    # Connect tcp client socket to the tcp server socket
                    ssock.connect(address)
                    # Receive data from server (i.e., current server time)
                    client.log("JEE!")
        except OSError as e:
            client.log(str(e), error=True)
        except Exception as e:
            client.log(str(e), error=True)
            

if __name__ == '__main__':
    pem = '/home/reijo/Desktop/DS_project/Certificates/server.pem'
    client = Client(pem)
    client._main()