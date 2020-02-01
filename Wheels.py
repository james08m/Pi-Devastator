import RPi.GPIO as GPIO

############################
## Wheels Interface Class ##
############################
class Wheels():

    # Initialise wheels
    def __init__(self, logger, pin_a1, pin_a2, pin_b1, pin_b2):
        self.logger = logger
        self.logger.info("[ Wheels ]\t Initialisation..")

        # Assigning pins motor A
        self.pin_motor_a1 = pin_a1
        self.pin_motor_a2 = pin_a2

        # Assigning pins motor B
        self.pin_motor_b1 = pin_b1
        self.pin_motor_b2 = pin_b2

        try:
            # Setting up GPIO pins
            self.logger.info("[ Wheels ]\t Setting up GPIO pins ")
            GPIO.setup(self.pin_motor_a1, GPIO.OUT)
            GPIO.setup(self.pin_motor_a2, GPIO.OUT)
            GPIO.setup(self.pin_motor_b1, GPIO.OUT)
            GPIO.setup(self.pin_motor_b2, GPIO.OUT)
        except e:
            self.logger.error("[ Wheels ]\t " + e)


    # Set motor A GPIOs values
    def setMotorA(self, pin_1, pin_2):
        try:
            GPIO.output(self.pin_motor_a1, pin_1)
            GPIO.output(self.pin_motor_a2, pin_2)
        except e:
            self.logger.error("[ Wheels ]\t " + e)

    # Set motor A GPIOs values
    def setMotorB(self, pin_1, pin_2):
        try:
            GPIO.output(self.pin_motor_b1, pin_1)
            GPIO.output(self.pin_motor_b2, pin_2)
        except e:
            self.logger.error("[ Wheels ]\t " + e)

    # Directionals methods
    def goFoward(self):
        self.setMotorA(False, True)
        self.setMotorB(False, True)

    def goBackward(self):
        self.setMotorA(True, False)
        self.setMotorB(True, False)

    def turnRight(self):
        self.setMotorA(True, False)
        self.setMotorB(False, True)

    def turnLeft(self):
        self.setMotorA(False, True)
        self.setMotorB(True, False)

    # All stop
    def stop(self):
        self.setMotorA(False, False)
        self.setMotorB(False, False)
