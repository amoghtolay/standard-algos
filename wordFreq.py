'''
Written in a few minutes for Evernote's codesprint on interviewstreet
Read a list of words, and then output them in some order depending 
on their frequency of occurence
'''

from collections import Counter, defaultdict

n = (int)(raw_input())
wordList = []

for i in range(n):
	wordList.append(raw_input())

cnt = Counter(wordList)
k = (int)(raw_input())

# invert the wordfreq dictionary so keys are
# frequency of occurrence and values are the words
freqword = defaultdict(list)
for word, freq in cnt.items():
    freqword[freq].append(word)

# print in order of occurrence
occurrences = freqword.keys()
occurrences.sort()
j = 0
for freq in reversed(occurrences):
	freqword[freq].sort() # sort words in list
	for i in freqword[freq]:
		j = j+1
		if (j<=k):
			print i
