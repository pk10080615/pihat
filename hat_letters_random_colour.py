#!/usr/bin/env python
# this script will display letters with random colours
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# assign a random integer between 0 and 255 to a variable named r
r = random.randint(0,255)
a = random.randint(0,255)
n = random.randint(0,255)

sense.show_letter("H", (r,a,n))
time.sleep(1)
sense.show_letter("i", (a,r,n))
time.sleep(1)
sense.show_letter("!", (a,n,r))
time.sleep(1)

sense.clear()
