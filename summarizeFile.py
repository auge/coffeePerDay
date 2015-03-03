#!/usr/bin/env python

import sys
import argparse
from operator import add

def arguments():
	"""
	parsing command line arguments
	"""
	parser = argparse.ArgumentParser(description="Summarize columns in given file.")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Print debug info.")
	parser.add_argument("-f", "--file", action="store", dest="filename", help="Path to file to read. Defaults to STDIN.")
#	parser.add_argument("-s", "--separator", dest="separator", default=",", help="Specify the separation character. Defaults to comma (,).")

	return parser.parse_args()

def main(args):
	"""
	integrating power readings from the given file (defaults to STDIN)
	required parameters (see arguments): separator, dataCol, pTime, pLimit
	"""
	if args.verbose:
		print(args)

	s = []

	if args.filename:
		if args.verbose:
			print("Opening " + args.filename)
		sys.stdin = open(args.filename)

	for line in sys.stdin:
#		line = [float(s) for s in line.split()]
		line = list(map(float, line.split()))
		if not s:
			s = line
		else:
			s = [a+b for a,b in zip(s, line)]

	sys.stdin.close()
	print("\t".join(str(i) for i in s))

if __name__ == '__main__':
	args = arguments()
	main(args)
