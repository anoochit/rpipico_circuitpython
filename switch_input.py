import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.GP25)
led.direction = Direction.OUTPUT


switch = DigitalInOut(board.GP20)
switch.direction = Direction.INPUT
switch.pull = Pull.UP


while True:
    if not switch.value:
        led.value = True
    else:
        led.value = False

    print('---')
    time.sleep(0.01)
