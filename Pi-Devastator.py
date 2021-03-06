import RPi.GPIO as GPIO
import os
import pygame
import sys
import datetime
import time
import logging

from Wheels import *
from Light import *
from RangeSensor import *
from Direction import * 

PIN_MOTOR_A1 = 29
PIN_MOTOR_A2 = 31
#PIN_MOTOR_A3 = 32
PIN_MOTOR_B1 = 36
PIN_MOTOR_B2 = 37
#PIN_MOTOR_B3 = 33
PIN_LIGHT = 22
PIN_TRIGGER = 11
PIN_ECHOE = 13

###############################
## PiDevastator Main Program ##
###############################
if __name__ == "__main__":

    ####################################
    ## Set Logger and Console Handler ##
    ####################################

    # Get actual date and set path and file name for the log
    date = datetime.datetime.now()
    file_path = "/home/pi/Pi-Devastator/log/{}{}".format(date.strftime("%Y-%m-%d"), ".log") # Log file for every day

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
    PiShutdown = False

    ####################
    ##  Set GPIO Mode ##
    ####################

    logger.info("[Devastator]\t Setting GPIO mode to BOARD")
    GPIO.setmode(GPIO.BOARD)
    
    ########################
    ##  Robot Components  ##
    ########################

    # Initisalise Direction
    direction = Direction.NONE 

    # Inititialise wheels
    wheels = Wheels(logger, PIN_MOTOR_A1, PIN_MOTOR_A2, PIN_MOTOR_B1, PIN_MOTOR_B2)
    wheels.stop() # Make sure wheels don't move

    # Inititialise status light
    light = Light(logger, PIN_LIGHT)

    # Initialise RangeSensor and start thread
    range_sensor = RangeSensor(logger, PIN_TRIGGER, PIN_ECHOE)
    range_sensor.start()

    # Signal components initialisation is completed
    light.flash(3)
    light.turnOn()

    #######################
    ## Initialise pygame ##
    #######################
    pygame.init()
    pygame.display.set_mode((1, 1))

    #############################
    ## Pi-Devastator main loop ##
    #############################
    while(PiDevastator_On):

    	# Display distance 
        print(range_sensor.getDistance())
        
        # Pygame event loop
        for event in pygame.event.get():
            
            # Event keys down
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    PiDevastator_On = False
                    range_sensor.stop()

                elif event.key == pygame.K_s:
                    PiShutdown = True
                    range_sensor.stop()
                    PiDevastator_On = False

                elif event.key == pygame.K_UP:
                    direction = Direction.FRONT
                    wheels.goFoward()

                elif event.key == pygame.K_DOWN:
                    direction = Direction.BACK
                    wheels.goBackward()

                elif event.key == pygame.K_LEFT:
                    direction = Direction.LEFT
                    wheels.turnLeft()

                elif event.key == pygame.K_RIGHT:
                    direction = Direction.RIGHT
                    wheels.turnRight()

                else:
                    pass

            # Event keys up        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    wheels.stop()
                elif event.key == pygame.K_DOWN:
                    wheels.stop()
                elif event.key == pygame.K_LEFT:
                    wheels.stop()
                elif event.key == pygame.K_RIGHT:
                    wheels.stop()

    
    # Wait for the RangeSensor thread to finish
    range_sensor.join()
    
    # Cleaning GPIO pins        
    logger.info("[Devastator]\t Cleaning all GPIO pins")
    GPIO.cleanup()

    # Log last entry for closure
    logger.info("[Devastator]\t Log closure")
    logger.info("--------------------------")
    logger.info("--------------------------")
        

    # Shutdown Raspberry Pi if requested
    if PiShutdown == True:
        time.sleep(0.1)
        logger.info("[ PI ]\t SHUTDOWN NOW")
        logger.info("[Devastator]\t Log closure")
        logger.info("--------------------------")
        logger.info("--------------------------")
        os.system('sudo shutdown now')