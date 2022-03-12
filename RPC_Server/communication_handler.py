class CommunicationHandler:
    
    
    def __init__(self,conn, addr):
        self.FORMAT = 'utf-8'
        self.connection = conn
        self.address = addr
        print("CommunicationHandler valmistettu")
        
        
        
    def send_message(self ,viesti):
        ####################################
        #Lähettää viestin clientille
        #
        ####################################

        message = viesti.encode(self.FORMAT)
        self.connection.send(message)

        return 0

