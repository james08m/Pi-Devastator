import RPi.GPIO as GPIO
import logging


#################################
#!# Not executed if imported  #!#
#################################
if __name__ == "__main__":

	#################################
	#!#      Setup debug log      #!#
	#################################

    # Get actual date and set path and file name for the log
    date = datetime.datetime.now()
    file_path = "./log/debug/{}{}".format(date.strftime("%Y-%m-%d"), ".debug") # Log file for every day

    # Uses %(<dictionary key>)s styled string substitution; the possible keys are documented in LogRecord attributes.
    log_format = "[ %(asctime)s ]\t[ %(levelname)s ]\t%(message)s" # Log format time-level-message

    # Create logger Object
    logger = logging.getLogger("Pi-Devastator Debug")
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
    logger.info("[Dev Debug]\t Debug log opened")

    # Setup GPIO Mode
    logger.info("[Dev Debug]\t Setting GPIO mode to BOARD")
	GPIO.setmode(GPIO.BOARD)

	# Cleaning GPIO pins in case previous program couldn't
	logger.info("[Dev Debug]\t Cleaning GPIO pins..")
	GPIO.cleanup()

	#################################
	#!# Add needed import bellow  #!#
	#################################
	#from Wheels import *
	#from Light import *
	#from RangeSensor import *


	#################################
	#!#   Code to execute / try   #!#
	#################################




	#################################
	#!#    Cleaning GPIO pins     #!#
	#################################
	logger.info("[Dev Debug]\t Cleaning GPIO pins..")
	GPIO.cleanup()

