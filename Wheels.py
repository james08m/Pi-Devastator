import RPi.GPIO as GPIO

class Wheels():
    
    # Initialise wheels
    def __init__(self, logger, pin_a1, pin_a2, pin_b1, pin_b2):
        self.logger = logger
        self.logger.info("[Wheels] - Initialisation..")
        
        # Assigning pins
        self.pin_motor_a1 = pin_a1
        self.pin_motor_a2 = pin_a2
        self.pin_motor_b1 = pin_b1
        self.pin_motor_b2 = pin_b2
        
        # Setting up GPIO pins
        self.logger.info("[Wheels] - Setting up GPIO pins")
        GPIO.setup(self.pin_motor_a1, GPIO.OUT)
        GPIO.setup(self.pin_motor_a2, GPIO.OUT)
        GPIO.setup(self.pin_motor_b1, GPIO.OUT)
        GPIO.setup(self.pin_motor_b2, GPIO.OUT)
    
    def setMotorA(self, pin_1, pin_2):
        GPIO.output(self.pin_motor_a1, pin_1)
        GPIO.output(self.pin_motor_a2, pin_2)
        
    def setMotorB(self, pin_1, pin_2):
        GPIO.output(self.pin_motor_b1, pin_1)
        GPIO.output(self.pin_motor_b2, pin_2)
        
    # Directions
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