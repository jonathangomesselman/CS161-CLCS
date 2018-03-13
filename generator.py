#!/usr/bin/env python

import math
import sys
from random import randint

def DNA(len):
	dna = ''
	letters = 'ATCG'

	for i in range(len):
		dna += letters[randint(0,3)]

	return dna

def main():
	args = sys.argv[1:]

	if args[0] == '-dna':
		len1 = int(args[1])
		len2 = int(args[2])

		print DNA(len1) + ' ' + DNA(len2)

	


if __name__ == '__main__':
	main()
