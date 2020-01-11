import RPi.GPIO as GPIO
import datetime
import time
import logging

#################################
#!# PiDevastator Main Program #!#
#################################

if __name__ == "__main__":

    # Get actual date and set path and file name for the log
    date = datetime.datetime.now()
    file_path = "./log/{}{}".format(date.strftime("%Y-%m-%d"), ".log") # Log file for every day

    # Uses %(<dictionary key>)s styled string substitution; the possible keys are documented in LogRecord attributes.
    log_format = "[ %(asctime)s ]\t[ %(levelname)s ]\t%(message)s" # Log format time-level-message

    # Create logger Object
    logger = logging.getLogger("Pi-Devastator Log")
    logging.basicConfig(format=log_format,
                        filename=file_path)  # Pass the filename and the log strings format used in file logs
    logger.setLevel(logging.DEBUG)  # Set logging level to DEBUG

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Can select a different logging lvl for the console if needed

    # Create formatter
    formatter = logging.Formatter(log_format) # Using log_format created above

    # Add the formatter to console handler
    console_handler.setFormatter(formatter)

    # Add the console handler to logger
    logger.addHandler(console_handler)

    logger.info("Pi-Devastator Log opened")

    # GPIO and PINs Initialisation
    logger.debug("GPIO and PINs Initialisation")
    GPIO.setmode(GPIO.BOARD)

    PIN_MOTOR_1_FORWARD = 7
    PIN_MOTOR_1_BACKWARD = 11
    PIN_MOTOR_2_FORWARD = 13
    PIN_MOTOR_2_BACKWARD = 15
    PIN_LIGHT_1 = 16
    PIN_LIGHT_2 = 18
    PIN_IR_RECEIVER = 22

    GPIO.setup(PIN_MOTOR_1_FORWARD, GPIO.OUT)
    GPIO.setup(PIN_MOTOR_1_BACKWARD, GPIO.OUT)
    GPIO.setup(PIN_MOTOR_2_FORWARD, GPIO.OUT)
    GPIO.setup(PIN_MOTOR_2_BACKWARD, GPIO.OUT)
    GPIO.setup(PIN_LIGHT_1, GPIO.OUT)
    GPIO.setup(PIN_LIGHT_2, GPIO.OUT)
    GPIO.setup(PIN_IR_RECEIVER, GPIO.INPUT)

    PiDevastator_On = True
    while(PiDevastator_On):
        print "do work"

    GPIO.cleanup() # Clear all GPIO pins for next utilisation

    logger.info("Pi-Devastator Log closure")

