from time import sleep
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

# Set up input pin
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Callback function to run when motion detected
def motionSensor(channel):
    if GPIO.input(21):     # True = Rising
        print('Motion Detected in ' + time.strftime("%d.%m.%Y %H:%M:%S"))

# add event listener on pin 21
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=300) 
counter = 0

try:
    while True:
        sleep(1)         # wait 1 second

finally:                   # run on exit
    GPIO.cleanup()         # clean up
    print "All cleaned up."