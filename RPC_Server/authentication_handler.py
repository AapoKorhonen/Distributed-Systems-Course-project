import error_handler

class AuthenticationHandler:

    def __init__(self, database):
        self._error = error_handler.ErrorHandler()
        self._database = database


    def check_authentication(self, username, password):

        try:
            if self._database._check_credentials(username, password):
                return True
            else:
                return False
        except Exception as e:
            respond_body = "Error in AuthenticationHandler._check_authentication!"
            self._error.print_error(e, respond_body)
            return False