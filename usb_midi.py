import time
import random
import usb_midi
import adafruit_midi
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

key1 = DigitalInOut(board.GP20)
key1.direction = Direction.INPUT
key1.pull = Pull.UP

key2 = DigitalInOut(board.GP21)
key2.direction = Direction.INPUT
key2.pull = Pull.UP

key3 = DigitalInOut(board.GP22)
key3.direction = Direction.INPUT
key3.pull = Pull.UP

print("Midi test")

# Convert channel numbers at the presentation layer to the ones musicians use
print("Default output channel:", midi.out_channel + 1)

# Software sythesis
# https://nicroto.github.io/viktor/

# Midi monitor
# https://www.midimonitor.com/#

def sendKey(key):
    midi.send(NoteOn(key, 60))
    time.sleep(0.25)
    midi.send([NoteOff(key, 127)])
    time.sleep(0.2)


while True:
    if not key1.value:
        sendKey("C5")
    if not key2.value:
        sendKey("D5")
    if not key3.value:
        sendKey("E5")

    time.sleep(0.01)
    print('---')
