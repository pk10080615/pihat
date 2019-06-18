#!/usr/bin/env python
# this script will show a scrolling message on the Pi HAT
# we imported time so it will rest in between the two messages
from sense_hat import SenseHat
import time
sense = SenseHat()

# sends the text Hello A&M! and How are you? to the show_message() function
sense.show_message("Hello A&M!")
time.sleep(1)
sense.show_message("How are you?")

