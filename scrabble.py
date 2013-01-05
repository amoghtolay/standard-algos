########################################################################
# THIS IS AN INCOMPLETE CODE. WORK ON THIS TO FINISH IT
########################################################################
'''
Amogh Tolay
Sun, 23rd Dec. 2012
Quora challenge named Scrabble StepLadder
http://www.quora.com/challenges#scrabble_stepladder
This is not a complete code
'''
import itertools

# Function to check if the two given words differ by exactly one letter
def stepLadder (word1, word2):
	flag = 0
	for i in range(len(word1)):
		if word1[i] is not word2[i]:
			flag = flag + 1
	if flag == 1:
		ans = True
	else:
		ans = False
	return ans

# Function to prune graph (remove nodes which can't act as center elems
def pruneGraph (graph):
	delKey = []
	
	for key in graph:
		removeAdjWord = []
		lessElm = 0
		centerScore = key[1]
		for adjWord in graph[key]:
			if adjWord[1] < centerScore:
				lessElm = lessElm + 1
			else:
				removeAdjWord.append(adjWord)
		# removing all nodes which are greater than key
		removeAdjWord = list(set(removeAdjWord))
		if (len(removeAdjWord)) is not 0:
			for delWord in removeAdjWord:
				graph[key].remove(delWord)
		graph[key].sort()
		# removing keys which don't have atleast 2 lesser nodes
		# ie. center elem (1 lesser for each side)
		if lessElm < 2:
			delKey.append(key)
		
	for key in delKey:
		del graph[key]
	
	return graph

# Take Input and after this, you have a list of unique words and their
# scrabble score as a tuple in a list
# Function to take input, calculate the scrabble score
# and make and return a list of words which are relevant(correct length)
def inputAndSort():
	# k denotes k lettered words to be considered
	# n denotes number of words that follow
	k = int(raw_input())
	n = int(raw_input())

	# listWords consists of list of all useful words that can be used in
	# the scrabble game according to k
	listWords = []

	# Iterate to get all words
	'''
	1 points: A, E, I, L, N, O, R, S, T, U
	2 points: D, G
	3 points: B, C, M, P
	4 points: F, H, V, W, Y
	5 points: K
	8 points: J, X
	10 points: Q, Z
	'''
	for count in range(n):
		word = raw_input()
		# if word length is correct, then you can add to list
		if len(word) is k:
			score = 0
			word = word.upper()
			
			# computing scrabble score
			for character in word:
				if character is 'A' or character is 'E' or character is 'I' or character is 'L' or character is 'N' or character is 'O' or character is 'R' or character is 'S' or character is 'T' or character is 'U':
					score = score + 1
				elif character is 'D' or character is 'G':
					score = score + 2
				elif character is 'B' or character is 'C' or character is 'M' or character is 'P':
					score = score + 3
				elif character is 'F' or character is 'H' or character is 'V' or character is 'W' or character is 'Y':
					score = score + 4
				elif character is 'K':
					score = score + 5
				elif character is 'J' or character is 'X':
					score = score + 8
				elif character is 'Q' or character is 'Z':
					score = score + 10
			listWords.append((word,score))
		listWords = list(set(listWords))
	return listWords

# Given a scrabble score of center element, calculates the upper bound
# of score that is possible with that as center
def upperBound ( value ):
	ub = pow((value-1),2) + (value-1) + value
	return ub

def branchBoundDFS ( graph ):
	# For every key (center element), choose two elements i and j which
	# are neighbours to this center element, and then perform dfs on
	# these two elements too
	maxScoreMult = 0
	for key in graph:
		for i in range(len(graph[key])):
			for j in range(len(graph[key])):
				sumPair = doubleDFS ( graph, maxScoreMult, i, j, key[1], key )
				maxScoreMult = max( maxScoreMult, sumPair )
	return maxScoreMult

# Perform double DFS starting from i and j
# Terminate when upper bound becomes less than max score till now
def doubleDFS ( graph, maxScore, i, j, nodeScore, key ):
	print key, i, j
	if ( upperBound (graph[key][i][1]) + upperBound (graph[key][j][1]) + nodeScore ) > maxScore:
		nodeScore = nodeScore + graph[key][i][1] + graph[key][j][1]
		for nodeLeft in graph[i]:
			for nodeRight in graph[j]:
				doubleDFS ( graph, maxScore, nodeLeft[1], nodeRight[1], nodeScore, key )
	return nodeScore


# Main code execution
listWords = inputAndSort()
pairs = list(itertools.permutations(listWords, 2))
# Now detect pairs and make graph also
graph =  {}
maxSingleton = ('',0)
for node in listWords:
	graph[node] = []
	if node[0][1] > maxSingleton[1]:
		maxSingleton = node
for x in pairs:
	if stepLadder(x[0][0], x[1][0]):
		graph [x[0]].append(x[1])
# Prune graph to remove nodes which can't be a center element
graph = pruneGraph (graph)
print graph

# Now start Branch and Bound DFS on the graph
# graph pruned for optimisation

maxScoreMult = branchBoundDFS (graph)

# Last step before output, please check with maxSingleton also
maxScore = max(maxScoreMult,maxSingleton)
print maxScore
