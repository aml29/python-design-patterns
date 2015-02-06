'''
    Implementation of command pattern
'''
class CreditCardManager:
    '''
        Invoker
    '''
    def set_authorization_command(self, authorization_command):
        self.authorization_command = authorization_command

    def set_capture_command(self, capture_command):
        self.capture_command = capture_command

    def authorize(self, data):
        self.authorization_command.execute(data)

    def capture(self, data):
        self.capture_command.execute(data)

class AuthorizationCommand:
    '''
        Authorization command
    '''
    def __init__(self, command):
        self.command = command

    def execute(self, data):
        self.command.authorize(data)

class CaptureCommand:
    '''
        Capture command
    '''
    def __init__(self, command):
        self.command = command

    def execute(self, data):
        self.command.capture(data)

class ConcreteCreditCardProvider:
    '''
        Concrete credit card provider
    '''
    def authorize(self, data):
        print("Authorization for {} is performed.".format(data['card']))

    def capture(self, data):
        print("{} euro captured from {}.".format(data['money'], data['card']))

if __name__ == "__main__":
    data = {
        'card' : "55554444333322221111",
        'money' : 20
    }

    provider = ConcreteCreditCardProvider()
    authorization_command = AuthorizationCommand(provider)
    capture_command = CaptureCommand(provider)

    cc_manager = CreditCardManager()
    cc_manager.set_authorization_command(authorization_command)
    cc_manager.set_capture_command(capture_command)
    cc_manager.authorize(data)
    cc_manager.capture(data)

    '''
        Output
        Authorization for 55554444333322221111 is performed.
        20 euro captured from 55554444333322221111.
    '''