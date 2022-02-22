"""
This is Rock-Paper-Scissors server.

https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
https://www.freecodecamp.org/news/python-property-decorator/ # @property lesson
"""


import datetime
import socket
import ssl
import error_handler


class RPCServer:
    def __init__(self, database, pem, key):
        self._database = database
        self._pem = pem
        self._key = key

    def _create_socket(self): # leading '_' in the method name distinguishes 
                                # private and public methods
        try:
            hostname = '127.0.0.1' # loopback address
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(server._pem, server._key) # give certificate and private key

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
                sock.bind((hostname, 8001))
                sock.listen(5)
                while True:
                    # Keep accepting connections from clients
                    with context.wrap_socket(sock, server_side=True) as ssock:
                        # (clientConnection, clientAddress) = serverSocket.accept()
                        conn, addr = ssock.accept()
                        print(conn.getpeercert)
                        # Send current server time to the client
                        serverTimeNow = "%s"%datetime.datetime.now()
                        conn.send(serverTimeNow.encode())
                        print("Sent %s to %s"%(serverTimeNow, addr))
                        # Close the connection to the client
                        conn.close()
        except OSError as e:
            respond_body = "OSError in _create_socket method!"
            handler = error_handler.ErrorHandler() # make an instance of the class ErrorHandler
            handler.print_error(e, respond_body)
        except Exception as e:
            respond_body = "Error in _create_socket method!"
            handler = error_handler.ErrorHandler() # make an instance of the class ErrorHandler
            handler.print_error(e, respond_body)

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
        """This method calls all the necessary classes to 
        run the server."""
        server = RPCServer(self._database, self._pem, self._key)
        server.log("Creating socket connection...")
        server._create_socket()
        server.log("Creating game handler...")

        


if __name__ == '__main__':
    """Server can be run only directly calling the 
    RPC_Server class."""
    pem = 'Certificates/server.pem'
    key = 'Certificates/server.key'

    server = RPCServer("database.db", pem, key)
    server._main()