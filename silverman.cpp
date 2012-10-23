/*
 * For O(logn), competition of Tower Research
 * Question was to calculate the sum of DJ(i^3) where DJ sequence is
 * defined as follows:
 * DJ[i] = num of times i occurs in the sequence (DJ is a non-decreasing
 * integer valued sequence)
 * i: 		1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16....
 * Dj[i]: 	1 2 2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 ....
 * Calculate DJ[i^3]
 * Solution presented here is brute force and not satisfactory
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int series(int n)
{
	long long sum = 0;
	
	int* num = new int[n*n*n];
	num[1] = 1;
	
	for (long long i = 1; i<(n*n*n); i++)
	{
		num[i+1] = 1 + num[ (i+1 - num[num[i]]) ];
	}
	for (long long i = 1; i<=n; i++)
		sum += num[i*i*i];
	
	delete num;
	return sum;
}

int main()
{
	int T;
	scanf("%d",&T);
	int n;
	for (int i=0; i<T; i++)
	{
		scanf("%d",&n);
		int sum = series(n);
		printf("%d\n", sum);
		
	}
	return EXIT_SUCCESS;
}
