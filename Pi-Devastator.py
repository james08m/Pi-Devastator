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
     # Set a delay to screen.getch()
     # Value to be determined (need phisical test) nodelay will probably to de work with the Counter implemented
    curses.halfdelay(5)
    #curses.noecho()
    screen.keypad(True)

    # Event loop
    # Counter implemented to stop wheels smoothly when key released
    no_key_pressed_count = 0
    while(PiDevastator_On):
        char = screen.getch()

        if char == ord('q'):
            PiDevastator_On = False;
        elif char == curses.KEY_UP:
            no_key_pressed_count = 0
            wheels.goFoward()
        elif char == curses.KEY_DOWN:
            no_key_pressed_count = 0
            wheels.goBackward()
        elif char == curses.KEY_RIGHT:
            no_key_pressed_count = 0
            wheels.turnRight()
        elif char == curses.KEY_LEFT:
            no_key_pressed_count = 0
            wheels.turnLeft()
        else:
            no_key_pressed_count++
            if no_key_pressed_count > 10: # Coutner value to determined (need phisical test)
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
