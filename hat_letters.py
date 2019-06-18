#!/usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)

sense.show_letter("H", red)
time.sleep(0.5)
sense.show_letter("i", white)
time.sleep(0.5)
sense.show_letter("!", blue)
time.sleep(0.5)

sense.clear()
