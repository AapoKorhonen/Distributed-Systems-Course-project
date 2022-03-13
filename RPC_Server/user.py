import communication_handler
import error_handler


class User:
    
    def __init__(self, username, connection, address):
        self.username = username
        self._communication_handler = communication_handler.CommunicationHandler(connection, address)
        self._error = error_handler.ErrorHandler()

    def send_message(self, viesti):
        try:
            self._communication_handler.send_message(viesti)
            
        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in User._send_message method!"
            self._error.print_error(e, respond_body)
        return 0

    def recieve_message(self):

        try:
            message = self._communication_handler.recieve_message()
            return message
        except Exception as e:
            respond_body = "Error in User._send_message method!"
            self._error.print_error(e, respond_body)

            return "0"

    def get_username(self):

        return self.username
