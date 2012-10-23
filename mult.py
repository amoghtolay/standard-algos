'''
Written in a few minutes for Evernote's codesprint on interviewstreet
Given a list of numbers, output in place of each number, the product of 
entire array divided by that number. 
O(n) time
'''

from array import *

n = (int)(raw_input())
num = [];
prod = 1;
isZero1 = 0;
isZero2 = 0;

for i in xrange(n):
	val = (long)(raw_input())
	if (val != 0):
		num.append(val)
		prod = prod*val
	if (val == 0):
		num.append(val)
		if (isZero1 == 1):
			isZero2 = 1
		if (isZero1 == 0):
			isZero1 = 1

for i in num:
	if (i == 0 and isZero2 == 0 ):
		print prod
	if (i == 0 and isZero2 == 1 ):
		print 0
	if ( i != 0 and isZero1 == 1):
		print 0
	if (i != 0 and isZero1 == 0):
		print prod/i

