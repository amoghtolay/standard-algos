/*
 * Written in a few minutes for Evernote's codesprint on interviewstreet
 * This is an implementation of a circular buffer with a few operations
 * O(n) time
 */

#include <stdio.h>
#include <malloc.h>
#include <cstring>
#include <iostream>
#include <stdlib.h>

using namespace std;

void append(string *buf, int &start, int &end, int n, string value)
{
	if (start-end == 1)
	{
		start = (start + 1) % n;
		buf[end] = value;
		end = (end + 1) % n;
	}
	else if (end == n-1 && start == 0)
	{
		start = (start + 1) % n;
		buf[end] = value;
		end = (end + 1) % n;
	}
	else
	{
		buf[end] = value;
		end = (end + 1) % n;
	}
}

void remove(string *buf, int &start, int &end, int n, int removeNum)
{
	/*
	if (end >= start)
		start = start + removeNum;
	else if (end < start && start + removeNum < n)
		start = start + removeNum;
	else if (end < start && start + removeNum >= n)
		start = (removeNum + start) % n;
	*/
	start = (start + removeNum) % n;
}
	
	
void list(string *buf, int &start, int &end, int n)
{
	if (start != end)
	{
		if (start < end)
			for (int i=start; i<end; i++)
				cout<<buf[i]<<"\n";
		if (start > end)
		{
			for (int i=start; i<n; i++)
				cout<<buf[i]<<"\n";
			for (int i=0; i<end; i++)
				cout<<buf[i]<<"\n";
		}
	}
}
	
int main()
{
	int N;
	cin>>N;
	++N;
	string buf[N];
	int start = 0, end = 0;
	while (true)
	{
		string cmd;
		int arg;
		cin>>cmd;
		
		if ( cmd == "Q" )
			exit(EXIT_SUCCESS);
		
		if (cmd == "A")
		{
			cin>>arg;
			string input;
			for (int i=0; i<arg; i++)
			{
				cin>>input;
				append(buf, start, end, N, input);
			}
		}
		if ( cmd == "R")
		{
			cin>>arg;
			remove(buf, start, end, N, arg);
		}
		if ( cmd == "L")
		{
			list(buf, start, end, N);
		}
	}
	return 0;
}
