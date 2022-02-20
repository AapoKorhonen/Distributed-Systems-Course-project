"""This is Rock-Paper-Scissors server."""


class RPC_Server:
    def __init__(server, database, key):
        server.database = database
        server.key = key

    def main():
        """This method calls all the necessary classes to 
        run the server."""
        pass


if __name__ == '__main__':
    """Server can be run only directly calling the 
    RPC_Server class."""
    server = RPC_Server("database.db", "keystore.jks")
    server.main()
