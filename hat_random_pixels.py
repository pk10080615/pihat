#!/usr/bin/env python
# this program will pick a random pixel and turn it on with another random colour
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

r= random.randint(0,7)
r2 = random.randint(0,7)

x = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

for i in range(0,10):

    sense.set_pixel(r,r2, (x,g,b))
    time.sleep(0.5)
    sense.set_pixel(r,r2, (0,0,0))
    time.sleep(0.5)

sense.clear()


