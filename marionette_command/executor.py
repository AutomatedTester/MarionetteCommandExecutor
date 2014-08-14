from marionette_transport.transport import MarionetteTransport


class MarionetteCommandExecutor(object):
    """ Command Executor that allows tight binding to the browser """
    def __init__(self, binary, profile, port):
        self.binary = binary
        self.profile = profile
        self.session_id = None
        PORT = port
        self.profile.port = PORT
        self.profile.update_preferences()
        self.binary.launch_browser(self.profile)
        self.transport = MarionetteTransport('127.0.0.1', PORT)
        self.transport.connect()

    def execute(self, command, params=None):
        message = {"name": command}
        if params:
        message["parameters"] = params
        response = self.transport.send(message)
        return response