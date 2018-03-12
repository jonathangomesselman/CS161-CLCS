

'''
for i in range (startRow, startRow + m + 1):
	for j in range(n + 1):
		print arr[i][j],
	print 
'''

# Using the LCS defined in LCS.py
# Used to compute P_0
def LCS(A,B, m):
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return arr[m][n]

# Using the LCS defined in LCS.py
# Used to compute P_0
def LCS_back(A,B, m):
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
				back_pts[i][j] = 2
			elif arr[i-1][j] >= arr[i][j-1]: # go up
				arr[i][j] = arr[i-1][j]
				back_pts[i][j] = 1
			else: # Go left
				arr[i][j] = arr[i][j-1]
				back_pts[i][j] = -1

	return arr[m][n]

# For a given end (row,col) backtrace to
# create the path that represents LCS
def backtrace_path_bounded(row, col, m, A, B, lowerPath, upperPath):
	# Store the actual length of LCS
	length = arr[row][col]

	# Perform the backtrace 
	# We want to go one further! This is an edge case
	endR = row - m
	#path_arr = [(0,0) for i in range(m)]
	# try paths as dic
	path = {}
	#while row != endR and col != 0:
		

	return (path, length)

# For a given end (row,col) backtrace to
# create the path that represents LCS
def backtrace_path(row, col, m, A, B):
	# Store the actual length of LCS
	length = arr[row][col]

	#print arr


	# Perform the backtrace 
	# We want to go one further! This is an edge case
	endR = row - m 
	#path_arr = [(0,0) for i in range(m)]
	# try paths as dic
	path = {}
	while row != endR and col != 0:
		# Mark how the column bounded by the path
		#path_arr[row - 1] = max(col, path_arr[row - 1])
		# If we are adding the upper bound
		if row not in path:
			path[row] = (col, col)
		else:
			path[row] = (col, path[row][1])
		# Take diagonal
		# Remember that we are 1 indexing
		if A[row - endR - 1] == B[col - 1]:
			row -= 1
			col -= 1
		elif col > 0 and arr[row][col - 1] >= arr[row - 1][col]: # Go left
			col -= 1
		else: # Go right
			row -= 1

	return (path, length)

# Creates a cut for the given string
def cut(str, i):
	return str[i:] + str[:i]



def findShortestPaths(A, B, paths, l, u, m):
	if u - l <= 1: return
	mid = (l + u) / 2
	#print mid
	#arr = np.zeros((4096, 4096), dtype=int)
	print 'top bound - %d' %(l)
	print paths[l]
	print 'bottom bound - %d' %(u)
	print paths[u]
	paths[mid] = singleShortestPath(A, B, mid, paths[l], paths[u], m)

	findShortestPaths(A, B, paths, l, mid, m)
	findShortestPaths(A, B, paths, mid, u, m)

def CLCS(A, B, m):
	# Clear array
	global arr
	arr = np.zeros((4096, 4096), dtype=int)

	# Paths
	paths = [(0,0) for i in range(m + 1)]
	# Compute p_0
	p_0 = LCS(A, B, m)
	paths[0] = backtrace_path(m, len(B), m, A, B)
	paths[m] = ({}, paths[0][1])
	for key in paths[0][0].keys():
		paths[m][0][key + m] = paths[0][0][key]
	#print paths[0]

	findShortestPaths(A, B, paths, 0, m, m)
	#print paths
	maximum = 0
	for path in paths:
		maximum = max(path[1], maximum)

	return maximum

def singleShortestPath(A, B, startRow, lowerPath, upperPath, m):
	n = len(B)

	#print 'starting'
	#print startRow
	# Clear out the rows right above the path 
	#for i in range(n + 1):
		#arr[startRow][i] = 0
	#for key in lowerPath[0].keys():
		#arr[]
	#global arr
	#arr = np.zeros((4096, 4096), dtype=int)
	
	arr[startRow:startRow + m, 1:] = 0
	print 'start row: %d' %(startRow + 1)
	
	for i in range(startRow + 1, startRow + m + 1):
		# define bounds
		aboveBound = lowerPath[0].get(i, (n,n))[1]
		bellowBound = upperPath[0].get(i, (1, 1))[0]
		print 'Start bound: %d, end bound: %d' % (bellowBound, aboveBound)
		for j in range(bellowBound, aboveBound + 1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				# Bound check
				#if j >= lowerPath[0].get(i, (n,n))[0]:
					#arr[i][j] = arr[i][j-1]
				#elif j == bellowBound:
					#arr[i][j] = arr[i-1][j]
				#else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])
			#print arr[i][j]
	#print 'ending'
	
	
	'''
	for i in range(startRow + 1, startRow + m + 1):
		# define bounds
		#aboveBound = lowerPath[0].get(i, (n + 1,n + 1))[1]
		#bellowBound = upperPath[0].get(i, (0, 0))[0]
		for j in range(1, n + 1):
			# We don't want to use previous elements
			#if j == 1:

			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1 if i != startRow + 1 else 1
				#arr[i][j] = arr[i-1][j-1]+1
			else:
				if i == startRow + 1:
					arr[i][j] = max(arr[i][j-1], 0)
				else:
					arr[i][j] = max(arr[i-1][j], arr[i][j-1])
			#print arr[i][j]
	'''
	
	print 'Start row: %d, value: %d' % (startRow, arr[startRow + m ][n])
	#return (0, arr[startRow + m ][n])
	#print arr[startRow + m][n]
	#print startRow
	#print arr
	#print backtrace_path(startRow + m, n, m-1, A, B)
	return backtrace_path(startRow + m, n, m-1, A, B) # m-1???
	#return backtrace_path_bounded(startRow + m, n, m, A, B, lowerPath, upperPath)


def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		# Here we should clear the array!!!!
		#print CLCS(A + A, B)
		#print CLCS(A + A, B, len(A))
		#LCS_back(A, B, len(A))
		#print backtrace_back_pointers(len(A), len(B))
		#print back_pts[:len(A)+1, :len(B)+1]
		print CLCS_back_pts(A + A, B, len(A))
		#print LCS(A, B)
		#print backtrace_path(7, 6, 7, A, B)


