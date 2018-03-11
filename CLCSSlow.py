#!/usr/bin/env python

import math
import sys

import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return arr[m][n]

	
# Creates a cut for the given string
def cut(str, i):
	return str[i:] + str[:i]

def CLCS(A, B):
	if len(A) > len(B):
		tmp = A
		A = B
		B = A

	max_lcs = 0
	# Loop through all the cuts
	for i in range(len(A)):
		cutA = cut(A, i)
		max_lcs = max(max_lcs, LCS(cutA, B))

	return max_lcs


def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		print CLCS(A, B)

if __name__ == '__main__':
	main()