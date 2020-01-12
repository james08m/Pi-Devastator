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
    logger.info("[Devastator]\t Log opened")
    logger.info("[Devastator]\t Starting Pi-Devastator")
    
    PiDevastator_On = True

    # GPIO Mode
    logger.info("[Devastator]\t Setting GPIO mode to BOARD")
    GPIO.setmode(GPIO.BOARD)

    # Inititialise components
    wheels = Wheels(logger, PIN_MOTOR_A1, PIN_MOTOR_A2, PIN_MOTOR_B1, PIN_MOTOR_B2)
    wheels.stop() # Make sure wheels don't move 
    
    light = Light(logger, PIN_LIGHT)
    
    # Signal initialisation complete
    light.flash(3)
    light.turnOn()
    
    # Initialise curses screen
    screen = curses.initscr()
    curses.cbreak()
    curses.halfdelay(5) # set a delay to screen.getch() 
    #curses.noecho()
    screen.keypad(True)

    # Event loop
    while(PiDevastator_On):
        char = screen.getch()
       
        if char == ord('q'):
            PiDevastator_On = False;
        elif char == curses.KEY_UP:
            wheels.goFoward()
        elif char == curses.KEY_DOWN:
            wheels.goBackward()
        elif char == curses.KEY_RIGHT:
            wheels.turnRight()
        elif char == curses.KEY_LEFT:
            wheels.turnLeft()
        elif char == ord('p'):
            wheels.stop()
        else:
            wheels.stop()
       
           

    logging.info("[Devastator]\t Closing curses..")
    screen.keypad(False)
    curses.nocbreak()
    #curses.echo()
    curses.endwin()
    logging.info("[Devastator]\t Closing curses..")
    
    logger.info("[Devastator]\t Cleaning GPIO pins..")
    GPIO.cleanup()

    logger.info("[Devastator]\t Log closure")

