#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(description="Scan through STDIN for periods where more than given amount of power has been consumed.")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Print debug info.")
parser.add_argument("-f", "--file", action="store", dest="filename", help="Path to file to read. Defaults to STDIN.")
parser.add_argument("-s", "--separator", dest="separator", default=",", help="Specify the separation character. Defaults to comma.")
parser.add_argument("-c", "--column", type=int, dest="dataCol", default=8, help="Specify the column of the input data that contains the data.")
parser.add_argument("-t", "--time", type=float, dest="pTime", default=20, help="Specify the time limit for counter in seconds.")
parser.add_argument("-p", "--power", type=float, dest="pLimit", default=500, help="Specify the power limit for the counter to be triggered.")

args = parser.parse_args()
if args.verbose:
	print args

prevPower = 0.0
risingTime = 0.0
coffees = 0

if args.filename:
	if args.verbose:
		print "Opening "+args.filename
	sys.stdin = open(args.filename)

for line in sys.stdin:
	items = line.split(args.separator)
	t_str = items[0]
	d_str = items[args.dataCol]
	if d_str == "NULL":
		pass
	try:
		time = float(t_str)
		power = float(d_str)

		if args.verbose:
			print "time: %f; power: %f" % (time, power)

		# rising edge:
		if prevPower < args.pLimit and power > args.pLimit:
			risingTime = time
		# falling edge:
		if prevPower > args.pLimit and power < args.pLimit:
			period = time - risingTime
			if args.verbose:
				print risingTime, (period)
			if period > args.pTime:
				coffees += 1
		# update power
		prevPower = power

	except ValueError:
		pass

sys.stdin.close()
print coffees
