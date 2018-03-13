#!/usr/bin/env python

import math
import sys

import numpy as np

# Pre-allocate the array
arr = np.zeros((4096, 2048), dtype=int)
# Have one array for the back-pointers
back_pts = np.zeros((2048, 2048), dtype=int)


def singleShortestPath_back_pointers(A, B, startRow, abovePath, belowPath):
	m = len(A) / 2
	n = len(B)

	for i in range(startRow + 1, startRow + m + 1):
		# Define bound
		# For the path above we want to take the 
		# second value in our tuple to search all
		# the way along a path on the same row.
		# If no path exists go till end of row
		aboveBound = abovePath[0].get(i, (n,n))[1]
		# For the path bellow we want to take
		# the first value in our path tuple to start
		# our search at the beginning of the path
		# for a given row. If the path doesn't
		# exist on that row start at index 1
		bellowBound = belowPath[0].get(i, (1, 1))[0]
		#print 'Start bound: %d, end bound: %d' % (bellowBound, aboveBound)
		for j in range(bellowBound, aboveBound + 1):
			back_pt_row = i - startRow
			if A[i-1] == B[j-1]: # Diag
				# Make sure that we do not use junk values when
				# We are first starting. Pretend as top row is all zeros
				arr[i][j] = arr[i-1][j-1]+1 if i != startRow + 1 else 1
				# Make sure to adjust row index to m x n table correspondence
				# for back pointers
				back_pts[back_pt_row][j] = 2
			else:
				above_cell = arr[i-1][j]
				if i == startRow + 1: # Avoid using dummy value of up cell
					above_cell = 0

				if j > abovePath[0].get(i, (n,n))[0]: # On the above boarder path so follow
					arr[i][j] = arr[i][j-1]
					back_pts[back_pt_row][j] = -1
				elif j == bellowBound: # On path so follow
					arr[i][j] = above_cell
					back_pts[back_pt_row][j] = 1
				elif above_cell >= arr[i][j-1]: # go up
					arr[i][j] = above_cell
					back_pts[back_pt_row][j] = 1
				else: # Go left
					arr[i][j] = arr[i][j-1]
					back_pts[back_pt_row][j] = -1

	path = backtrace_back_pointers(m, len(B), startRow)
	length = arr[startRow + m][n]

	return (path, length)


def backtrace_back_pointers(m, n, startRow):
	path = {}
	row = m
	col = n

	while row != 0 and col != 0:
		#print 'Row: %d Col: %d' %(row, col)
		if row + startRow not in path:
			path[row + startRow] = (col, col)
		else: # We are still in the same row so we want to change the upper/lower bound path values
			path[row + startRow] = (col, path[row + startRow][1])

		# -1 = go left (decrese col)
		# 1 = go up (decrese row)
		# 2 = diag
		if back_pts[row][col] == -1:
			col -= 1
		elif back_pts[row][col] == 1:
			row -= 1
		else:
			row -= 1
			col -= 1

	return path

def shortestPaths(A, B, paths, l, u):
	if u - l <= 1: return
	mid = (l + u) / 2
	paths[mid] = singleShortestPath_back_pointers(A, B, mid, paths[l], paths[u])

	shortestPaths(A, B, paths, l, mid)
	shortestPaths(A, B, paths, mid, u)

def CLCS_back_pts(A, B, m):
	# Paths
	paths = [(0,0) for i in range(m + 1)]
	# Compute p_0
	paths[0] = singleShortestPath_back_pointers(A, B, 0, ({}, 0), ({}, 0))
	# Assign p_m by just shifting p_0 down m units
	paths[m] = ({}, paths[0][1])
	for key in paths[0][0].keys():
		paths[m][0][key + m] = paths[0][0][key]

	shortestPaths(A, B, paths, 0, m)
	#print paths
	maximum = 0
	for path in paths:
		maximum = max(path[1], maximum)

	return maximum


def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		# Here we should clear the array!!!!
		print CLCS_back_pts(A + A, B, len(A))


if __name__ == '__main__':
	main()
