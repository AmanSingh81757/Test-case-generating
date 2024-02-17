# Python3 implementation to generate
# test-case for the Tree
import random

# Maximum Number Of Nodes
MAXNODE = 1000

# Maximum Number Of testCases
MAXT = 10

# Maximum weight
MAXWEIGHT = 100

# Function for the path
# compression technique
def find(parent, x):

	# If parent found
	if parent[x] == x:
		return x

	# Find parent recursively
	parent[x] = find(parent, parent[x])

	# Return the parent node of x
	return parent[x]

# Function to compute the union
# by rank
def merge(parent, size, x, y):
	r1 = find(parent, x)
	r2 = find(parent, y)

	if size[r1] < size[r2]:
		parent[r1] = r2
		size[r2] += size[r1]
	else:
		parent[r2] = r1
		size[r1] += size[r2]

# Function to generate the
# test-cases for the tree
def generate():

	# Number of testcases
	# t = random.randint(1, MAXT)
    t=1
	# print(t)
    for _ in range(t):
        n = random.randint(2, MAXNODE)
        print(n)
        parent = [i for i in range(n + 1)]
        size = [1 for _ in range(n + 1)]
        Edges = []
        weights = []
        for i in range(n):
            nom = random.randint(1, 1000)
            print(nom, end = ' ')
        print()
		# Now We have add N-1 edges
        for i in range(n - 1):
            x = random.randint(1, n)
            y = random.randint(1, n)

			# Find edges till it does not
			# forms a cycle
            while find(parent, x) == find(parent, y):
                x = random.randint(1, n)
                y = random.randint(1, n)

			# Merge the nodes in tree
            merge(parent, size, x, y)

			# Store the current edge and weight
            Edges.append((x, y))
            w = random.randint(1, MAXWEIGHT)
            weights.append(w)

		# Print the set of edges
		# with weight
        for i in range(len(Edges)):
            print(Edges[i][0], Edges[i][1])
        q = random.randint(1, 100000)
        print(q)
        for i in range(q):
            u = random.randint(1, n)
            v = random.randint(1, n)
            print(u, v)

# Driver Code
if __name__ == "__main__":

	# Uncomment the below line to store
	# the test data in a file
	# open("output.txt", "w").close()
	# open("output.txt", "w").write(generate())

	# For random values every time
	random.seed(None)

	generate()

# This code is contributed by Potta Lokesh
