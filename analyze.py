#!/usr/bin/env python

import fileinput
import argparse

verbose = False

parser = argparse.ArgumentParser(description="Scan through STDIN and list periods where more than 500 W of power were consumed")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="show debug info")

parser.parse_args()

prevPower = 0.0
risingTime = 0.0
coffees = 0

for line in fileinput.input():
	items = line.split(",")
	try:
		time = float(items[0])
		power = float(items[1])
	except ValueError:
		pass
	if verbose:
		print "time: %f; power: %f" % (time, power)
	# rising edge:
	if prevPower < 500 and power > 500:
		risingTime = time
	# falling edge:
	if prevPower > 500 and power < 500:
		period = time - risingTime
		if verbose:
			print risingTime, (period)
		if period > 20:
			coffees += 1
	
	# update power
	prevPower = power

print coffees
