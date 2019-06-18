#!/usr/bin/env python   
# this will show a matrix of colours
from sense_hat import SenseHat
import time
sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)

pixels = [
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w,
    w,w,b,w,w,w,w,w, 
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
]

sense.set_pixels(pixels)

time.sleep(3)
sense.clear()

