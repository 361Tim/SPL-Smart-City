
from LightSensor import LightSensor

class Receiver:
    def __init__(self,sendsignal):
        self.sensor = LightSensor()
        self.signal = sendsignal
        

