#!/usr/bin/env python
# this will roll dice
from random import randint
import random
import sys
min = 1

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
	max_num = input("How many sides should be on the dice?")
	max = int(max_num)
	dice = int(input("How many die should I roll?"))
	print "Rolling the dice..."
	print "The values are:"
	for number in range(0,dice):
		chosen = randint(min,max)
		print (chosen)

	roll_again = raw_input("Roll the dice again?")

if roll_again == "n" or roll_again == "no":
	sys.exit()
