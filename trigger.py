from gpiozero import OutputDevice
from time import sleep

class activate():
    def __init__(self):
        self.led = OutputDevice(4, active_high=True, initial_value=False, pin_factory=None)

    def trigger(self, time):
        self.led.on()
        sleep(time)
        self.led.off()
