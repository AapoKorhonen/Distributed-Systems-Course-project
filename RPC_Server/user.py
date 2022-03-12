import communication_handler

class User:
    
    def __init__(self, username, connection, address):
        self.username = username
        self._communication_handler = communication_handler.CommunicationHandler(connection, address)

        def send_message(self):
            # kutsutaan communication handleria...
            pass