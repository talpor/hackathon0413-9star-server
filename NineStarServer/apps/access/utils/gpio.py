import RPi.GPIO as GPIO
import time

def push_button(pin_number, sleep_time):
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.OUT)

    GPIO.output(pin_number, GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.output(pin_number, GPIO.LOW)
    time.sleep(1)

    GPIO.cleanup()
    return
    


