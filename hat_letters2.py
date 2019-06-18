#!/usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.show_letter("H", (255,0,0))
time.sleep(0.5)
sense.show_letter("i", (125,125,125))
time.sleep(0.5)
sense.show_letter("!", (0,255,0))
time.sleep(0.5)

sense.clear()
