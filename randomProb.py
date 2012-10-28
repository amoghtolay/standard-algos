'''
Amogh Tolay - 28th Oct 2012
This was a question in codesprint 3 on interviewstreet
There is an uniform prob distribution over [0,A] and [0,B]. Let the
random variables be X and Y. Find the prob that X+Y < C
Make probability distribution function and then the cummulative
distribution function
'''
import fractions

n = (int)(raw_input())

for i in range(n):
	s = raw_input()
	A,B,C = (fractions.Fraction( int(i) ) for i in s.split(' '))
	
	if A <= B:
		if C <= A:
			ans = fractions.Fraction( (C*C) / (2*A*B))
		if C > A and C <=B:
			ans = fractions.Fraction(((A*A)/2 + A*(C-A))/(A*B))
		if C > B and C <= A+B:
			ans = fractions.Fraction( ( (A*A)/2 + (B-A)*A + (A*C + B*C - C*C/2) - (A*B + B*B/2) ) / (A*B) )
		if C > (A+B):
			ans = 1
			
	if A > B:
		if C <= B:
			ans = fractions.Fraction( (C*C) / (2*A*B) )
		if C > B and C <=A:
			ans = fractions.Fraction( ((B*B)/2 + B*(C-B)) / (A*B) )
		if C > A and C <= A+B:
			ans = fractions.Fraction( ( (B*B)/2 + (A-B)*B + (A*C + B*C - C*C/2) - (A*A/2 + A*B) ) / (A*B) )
		if C > (A+B):
			ans = 1
	
	
	if str(ans) is '1':
		print "1/1"
	else:
		print ans
