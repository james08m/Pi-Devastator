import RPi.GPIO as GPIO
import time
import threading

class RangeSensor(threading.Thread):

    # Initialise wheels
    def __init__(self, logger, trigger, echo):
        threading.Thread.__init__(self)
        self.logger = logger
        self.logger.info("[RangeSensor]\t Initialisation..")
        self.pin_trigger = trigger
        self.pin_echo = echo

        self.running = True
        self.distance = 0
        self.previous_distance = 0

        # Setting up GPIO pins
        self.logger.info("[RangeSensor]\t Setting up GPIO pin")
        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)

        # Make sure trigger start low
        GPIO.output(self.pin_trigger, False)
        
    def getDistance(self):
        return self.distance

    def stop(self):
        self.running = False
        self.logger.info("[RangeSensor]\t Thread Stopped")


    def run(self):
        while self.running == True:

            # save last distance measured
            self.previous_distance = self.distance

            # set trigger to hight
            GPIO.output(self.pin_trigger, True)

            # set trigger to low after 0.01ms
            time.sleep(0.00001)
            GPIO.output(self.pin_trigger, False)

            # register when signal is sent (will quit loop by going to 1)
            while GPIO.input(self.pin_echo) == 0:
                start_time = time.time()

            # register when signal has returned (will quit loop by going to 0)
            while GPIO.input(self.pin_echo) == 1:
                end_time = time.time()

            # Calculate the time it took for the wave to come back
            elapsed_time =  end_time - start_time

            # * by sonic speed per cm (34300) and / by 2 has the wave travel the distance twice
            self.distance = (elapsed_time * 34300) / 2
            
            time.sleep(0.5)