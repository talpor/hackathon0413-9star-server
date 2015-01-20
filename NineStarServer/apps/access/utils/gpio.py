import RPi.GPIO as GPIO
import time

GATE_PIN = {
    '1': 11,
    '2': 13,
}

def open_gate(gate):
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GATE_PIN[gate], GPIO.OUT)

    GPIO.output(GATE_PIN[gate], GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GATE_PIN[gate], GPIO.LOW)
    time.sleep(1)

    GPIO.cleanup()
    return True
