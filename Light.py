import RPi.GPIO as GPIO
import time

#################
## Light Class ##
#################
class Light():

    # Initialise wheels
    def __init__(self, logger, pin):
        self.logger = logger
        self.logger.info("[ Light ]\t Initialisation..")
        self.pin = pin

        # Setting up GPIO pins
        self.logger.info("[ Light ]\t Setting up GPIO pin " + str(self.pin))
        GPIO.setup(self.pin, GPIO.OUT)

    def turnOn(self):
        GPIO.output(self.pin, True)

    def turnOff(self):
        GPIO.output(self.pin, False)

    def flash(self, value):
        self.logger.info("[ Light ]\t Flashing..")
        for x in range(value):
            self.turnOn()
            time.sleep(0.5)
            self.turnOff()
            time.sleep(0.5)
