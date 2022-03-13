import error_handler

class CommunicationHandler:
    
    
    def __init__(self,conn, addr):
        self.FORMAT = 'utf-8'
        self.HEADER = 64
        self.connection = conn
        self.address = addr
        self._error = error_handler.ErrorHandler()
        print("CommunicationHandler created")
        
        
        
    def send_message(self ,viesti):
        ####################################
        #Lähettää viestin clientille
        #
        ####################################
        try:
            message = viesti.encode(self.FORMAT)
            self.connection.send(message)

        # Muista lisätä tarkempi virheenkäsittely tarvittaessa!!!
        except Exception as e:
            respond_body = "Error in GameHandler._initialize_players method!"
            self._error.print_error(e, respond_body)
        return 0

    def recieve_message(self):

        try:
            message = self.connection.recv(self.HEADER).decode(self.FORMAT)
            while not message:
                message = self.connection.recv(self.HEADER).decode(self.FORMAT)

            return message

        except Exception as e:
            respond_body = "Error in User._send_message method!"
            self._error.print_error(e, respond_body)
            return "0"

