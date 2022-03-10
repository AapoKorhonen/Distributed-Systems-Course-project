"""
This is Rock-Paper-Scissors server.

https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
"""


import datetime
import socket
import ssl
import error_handler

import database
import communication_handler
import game_generator

class RPCServer:
    def __init__(self, pem, key):
        self._database = None
        self._pem = pem
        self._key = key
        self._error = error_handler.ErrorHandler()

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
                        # give here communication handler to the client
                        communication_handler.CommunicationHandler(conn, addr)

                        #print(conn.getpeercert)
                        # Send current server time to the client
                        #serverTimeNow = "%s"%datetime.datetime.now()
                        #conn.send(serverTimeNow.encode())
                        #print("Sent %s to %s"%(serverTimeNow, addr))
                        # Close the connection to the client
                        #conn.close()
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
        server = RPCServer(self._pem, self._key)
        server.log("Initializing database...")
        server._create_database()
        # you need to initialize other handlers before opening the socket connection
        server.log("Creating game generator...")

        server.log("Creating socket connection...")
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










