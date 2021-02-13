import time
import board
import usb_hid
from digitalio import DigitalInOut, Direction, Pull

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

switch = DigitalInOut(board.GP20)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

switch2 = DigitalInOut(board.GP21)
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    if not switch.value:
        print('y')
        keyboard.press(Keycode.LEFT_ALT, Keycode.F1)
        keyboard.release_all()

    if not switch2.value:
        print('y')
        keyboard.press(Keycode.LEFT_ALT, Keycode.F2)
        keyboard.release_all()

    print('---')
    time.sleep(0.2)
