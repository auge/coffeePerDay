#!/usr/bin/env python

import sys
import argparse

def arguments():
	"""
	parsing command line arguments
	"""
	parser = argparse.ArgumentParser(description="Integrate all columns of a data file. Time is in column 0.")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Print debug info.")
	parser.add_argument("-k", "--kwh", action="store_true", dest="kwh", default=False, help="output in kWh (instead of Ws)")
	parser.add_argument("-f", "--file", action="store", dest="filename", help="Path to file to read. Defaults to STDIN.")
	parser.add_argument("-s", "--separator", dest="separator", default=",", help="Specify the separation character. Defaults to comma (,).")

	return parser.parse_args()

def main(args):
	"""
	integrating power readings from the given file (defaults to STDIN)
	required parameters (see arguments): separator, dataCol, pTime, pLimit
	"""
	if args.verbose:
		print(args)

	energy = []
	prev_t = 0

	if args.filename:
		if args.verbose:
			print("Opening "+args.filename)
		sys.stdin = open(args.filename)

	for line in sys.stdin:
		items = line.split(args.separator)
		t_str = items.pop(0)
		if t_str == "timestamp":
			continue
		time = float(t_str)
		power = [0 if i.strip() == "NULL" else float(i) for i in items]

		if prev_t > 0:
			delta_t = time - prev_t
			if not energy:
				energy = [p * delta_t for p in power]
			else:
				energy = [e + p * delta_t for e,p in zip(energy, power)]

		# update time
		prev_t = time

	sys.stdin.close()
	if args.kwh:
		energy = [e / 3600000 for e in energy]
	print("\t".join(str(e) for e in energy))

if __name__ == '__main__':
	args = arguments()
	main(args)
