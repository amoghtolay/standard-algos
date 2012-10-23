/*
 * Written in a few minutes for Evernote's codesprint on interviewstreet
 * This code finds the 4 largest number in a continous stream of numbers
 * Done in O(n) time which it takes to imput numbers
 */


#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <climits>

using namespace std;

int main()
{
	int max1 = INT_MIN, max2 = INT_MIN, max3 = INT_MIN, max4 = INT_MIN;
	int n, number;
	cin>>n;
	for (int i=0; i<n; i++)
	{
		cin>>number;
		
		if (number >= max1)
		{
			int temp;
			temp = max1;
			max1 = number;
			
			max4 = max3;
			max3 = max2;
			max2 = temp;
		}
		
		if (number < max1 && number >= max2)
		{
			int temp;
			temp = max2;
			max2 = number;
			
			max4 = max3;
			max3 = temp;
		}
		
		if (number < max2 && number >= max3)
		{
			int temp;
			temp = max3;
			max3 = number;
			
			max4 = temp;
		}
		
		if (number < max3 && number >= max4)
		{
			max4 = number;
		}		
	}
	cout<<max1<<"\n"<<max2<<"\n"<<max3<<"\n"<<max4<<"\n";
	return EXIT_SUCCESS;
}

