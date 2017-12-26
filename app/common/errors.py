



class TwilioCredentialError(Exception):
    """
    Twilio Credentials Error class
    """
    def __str__(self):
        return _twilio_cred_msg


class FlaskNotifyEmailError(Exception):
    """
    Flask Notify email error class
    """
    pass


class FlaskNotifyAuthenticationError(Exception):
    """
    Flask Notify Authentication error class
    """
    def __str__(self):
        return 'Mailtrap SMTP credentials are wrong'
