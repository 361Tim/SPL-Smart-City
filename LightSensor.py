
class LightSensor:
    def __init__(self, receiver):
        self.receiver = receiver

    def sendSignal(self):

        self.receiver.data("lamp is on")