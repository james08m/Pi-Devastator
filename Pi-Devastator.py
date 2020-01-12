import RPi.GPIO as GPIO
import curses
import datetime
import time
import logging

from Wheels import *
from Light import *

PIN_MOTOR_A1 = 7
PIN_MOTOR_A2 = 11
PIN_MOTOR_B1 = 13
PIN_MOTOR_B2 = 15
PIN_LIGHT = 16

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
    logger.info("[Pi-Devastator] - Log opened")
    logger.info("[Pi-Devastator] - Starting Pi-Devastator")
    
    PiDevastator_On = True

    # GPIO Mode
    logger.info("[Pi-Devastator] - Setting GPIO mode to BOARD")
    GPIO.setmode(GPIO.BOARD)

    # Inititialise components
    wheels = Wheels(logger,
                    PIN_MOTOR_A1,
                    PIN_MOTOR_A2,
                    PIN_MOTOR_B1,
                    PIN_MOTOR_B2)
    
    light = Light(logger, PIN_LIGHT)
    
    # Initialise curses
    screen = curses.initscr()
    screen.keypad(True)
    
    # Signal initialisation complete
    light.flash(5)
    light.turnOn()

    # Event loop
    while(PiDevastator_On):
       char = screen.getch()
       
       if char == ord('q'):
           PiDevastator_On = False;

    logging.info("[Pi-Devastator] - Closing curses..")
    screen.keypad(False)
    curses.endwin()
    logging.info("[Pi-Devastator] - Closing curses..")
    
    logger.info("[Pi-Devastator] - Cleaning GPIO pins..")
    GPIO.cleanup()

    logger.info("[Pi-Devastator] - Log closure")

