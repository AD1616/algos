# Python3 program for the above approach

# Function to check if a vertex v
# can be added at index pos in
# the Hamiltonian Cycle
def isSafe(v, graph, path, pos):

	# If the vertex is adjacent to
	# the vertex of the previously
	# added vertex
	if graph[path[pos - 1]][v] == 0:
		return False

	# If the vertex has already
	# been included in the path
	for i in range(pos):
		if path[i] == v:
			return False

	# Both the above conditions are
	# not true, return true
	return True

# To check if there exists
# at least 1 hamiltonian cycle
hasCycle = False

# Function to find all possible
# hamiltonian cycles
def hamCycle(graph):
	global hasCycle
	
	# Initially value of boolean
	# flag is false
	hasCycle = False

	# Store the resultant path
	path = []
	path.append(0)

	# Keeps the track of the
	# visited vertices
	visited = [False]*(len(graph))

	for i in range(len(visited)):
		visited[i] = False

	visited[0] = True

	# Function call to find all
	# hamiltonian cycles
	FindHamCycle(graph, 1, path, visited)

	if hasCycle:
		# If no Hamiltonian Cycle
		# is possible for the
		# given graph
		print("No Hamiltonian Cycle" + "possible ")
		return

# Recursive function to find all
# hamiltonian cycles
def FindHamCycle(graph, pos, path, visited):

	# If all vertices are included
	# in Hamiltonian Cycle
	if pos == len(graph):
	
		# If there is an edge
		# from the last vertex to
		# the source vertex
		if graph[path[-1]][path[0]] != 0:
		
			# Include source vertex
			# into the path and
			# print the path
			path.append(0)
			for i in range(len(path)):
				print(path[i], end = " ")
			print()

			# Remove the source
			# vertex added
			path.pop()

			# Update the hasCycle
			# as true
			hasCycle = True
		return

	# Try different vertices
	# as the next vertex
	for v in range(len(graph)):
	
		# Check if this vertex can
		# be added to Cycle
		if isSafe(v, graph, path, pos) and not visited[v]:
			path.append(v)
			visited[v] = True

			# Recur to construct
			# rest of the path
			FindHamCycle(graph, pos + 1, path, visited)

			# Remove current vertex
			# from path and process
			# other vertices
			visited[v] = False
			path.pop()

def appender (finalArray, array, startingIndex): # appends an array onto another
    placeholder = finalArray
    for row in array:
        try:
            placeholder[startingIndex] += row   # does the actual appending
        except:
            print("didn't work")
            return placeholder  # catches if you accidentally went out of bounds
        startingIndex += 1

    return placeholder

a1 = [   # adjacency matrix Q3
    [0, 1, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0]
]

a2 = [   # identity matrix 8x8
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
]

b1 = [  # adjacency matrix Q4
      [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

b2 = [  # identity matrix 16x16
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

QFour = [  # initializing a 16x16 matrix
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

QFive = [   # initializing a 32x32 matrix
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

appender(QFour, a1, 0)
appender(QFour, a2, 0)
appender(QFour, a1, 8)
appender(QFour, a2, 8)  # call appender functions to actually populate the 16x16

appender(QFive, b1, 0)
appender(QFive, b2, 0)
appender(QFive, b1, 16)
appender(QFive, b2, 16) # call appender functions to actually populate the 32x32

hamCycle(QFour)
hamCycle(QFive)