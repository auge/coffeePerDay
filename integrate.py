#!/usr/bin/env python

import sys
import argparse

def arguments():
	"""
	parsing command line arguments
	"""
	parser = argparse.ArgumentParser(description="Scan through STDIN for periods where more than given amount of power has been consumed.")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Print debug info.")
	parser.add_argument("-k", "--kwh", action="store_true", dest="kwh", default=False, help="output in kWh (instead of Ws)")
	parser.add_argument("-f", "--file", action="store", dest="filename", help="Path to file to read. Defaults to STDIN.")
	parser.add_argument("-s", "--separator", dest="separator", default=",", help="Specify the separation character. Defaults to comma (,).")
	parser.add_argument("-c", "--column", type=int, dest="dataCol", default=8, help="Specify the column of the input data that contains the data. Defaults to column 8.")

	return parser.parse_args()

def main(args):
	"""
	integrating power readings from the given file (defaults to STDIN)
	required parameters (see arguments): separator, dataCol, pTime, pLimit
	"""
	if args.verbose:
		print(args)

	energy = 0
	prev_t = 0

	if args.filename:
		if args.verbose:
			print("Opening "+args.filename)
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
				print("time: %f; power: %f" % (time, power))

			if prev_t > 0:
				delta_t = time - prev_t
				energy += power * delta_t
				if args.verbose:
					print("delta_t: %f; energy: %f" % (delta_t, energy))

			# update time
			prev_t = time

		except ValueError:
			pass

	sys.stdin.close()
	if args.kwh:
		energy /= 3600000
	print(energy)

if __name__ == '__main__':
	args = arguments()
	main(args)
