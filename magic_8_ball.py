#!/usr/bin/env python
# this code works like a magic 8-ball, with 6 random responses!
import sys
import random

ans= True

while ans:
	question = raw_input("Ask the magic 8-ball a question: (press enter to quit)")
	
	answers = random.randint(1,8)

	if question == "":
		sys.exit()

	elif answers == 1:
		print ("Absolutely")

	elif answers == 2:
		print ("The chances are high")

	elif answers == 3:
		print ("Hmmm, it's possible")

	elif answers == 4:
		print ("I wouldn't count on it")

	elif answers == 5:
		print ("Ask again later")

	elif answers == 6:
		print ("Unfortunately, no.")
