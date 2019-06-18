#!/usr/bin/env python   
from sense_hat import SenseHat
sense = SenseHat()

# creating variables for colours
maroon = (240,0,175)
c_colour = (0,255,255)

speed= 0.05

message = "Hello A&M!"

# this passes the function the message, speed, and other variables
sense.show_message(message, speed, text_colour=maroon, back_colour=c_colour)

sense.clear()
