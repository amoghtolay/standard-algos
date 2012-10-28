'''
Amogh Tolay - 28th Oct 2012
This was a question in codesprint 3 on interviewstreet
Used DFS from an adjacency matrix
'''
# prints a depth-first-search from the starting node
def dfs(node):
	visited = set()
	visited.add(node)
	stack = []
	stack.append(node)
	conComp = []
	while len(stack) > 0:
		current = stack.pop()
		conComp.append(current)
		color[current] = 1
		for nodes in graph[current]:
			if nodes not in visited:
				stack.append(nodes)
				visited.add(nodes)
	return sorted(conComp)

n = (int)(raw_input())
s = raw_input()

a = ([int(i) for i in s.split(' ')])
color = []
for k in range(n+1):
	color.append(0)

graph={}

for i in range(n):
	s = raw_input()
	vertNum = 0
	graph[a[i]] = []
	for val in s:
		if val is 'Y':
			graph[a[i]].append(a[vertNum])
			vertNum+= 1
		if val is 'N':
			vertNum+= 1

connectedComp = []

for vert in a:
	if color[vert] is 0:
		connectedComp.append( dfs (vert) )

counter = []
index = len(connectedComp)

for i in range(index):
	counter.append(0)
finalAns = []

# Printing code - seems correct as of now
for element in a:
	for i in range(index):
		if element not in connectedComp[i]:
			continue
		finalAns.append(connectedComp[i][counter[i]])
		counter[i] += 1
print ' '.join(str(x) for x in finalAns)
