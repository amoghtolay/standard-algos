/*
 * For O(logn), competition of Tower Research
 * A Dijkstra's algorithm on graph where the graph is represented
 * as an adjacency matrix
 */

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <stdio.h>

#define INF 10000000

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int i=0; i<T; i++)
	{
		int numVert, numEdges;
		cin>>numVert>>numEdges;
		int graph[numVert][numVert];
		for (int j=0; j<numVert; j++)
			for (int k=0; k<numVert; k++)
				graph[j][k]=INF;
		
		for (int j=0; j<numEdges; j++)
		{
			int u,v,w;
			
			cin>>u>>v>>w;
			graph[u][v] = w;
		}
		
		// Graph complete
		int Q;
		cin>>Q;
		for (int j=0; j<Q; j++)
		{
			int s,target,cost;
			cin>>s>>target;
			
			/*
			 * DIJKSTRA's code here
			 */
			int dist[numVert];
			int selected[numVert];
			for (int j=0; j<numVert; j++)
			{
				selected[j] = 0;
				dist[j] = INF;
			}
			
			int m,min,start,d;
			start = s;
			selected[start]=1;
			dist[start] = 0;
			while(selected[target] ==0)
			{
				min = INF;
				m = 0;
				for(int i=0; i<numVert; i++)
				{
					d = dist[start] + graph[start][i];
					if(d< dist[i]&&selected[i]==0)
					{
						dist[i] = d;
					}
					if(min>dist[i] && selected[i]==0)
					{
						min = dist[i];
						m = i;
					}
				}
				start = m;
				selected[start] = 1;
			}

			cost = dist[target];
			// Ends here
			cout<<cost<<"\n";
		}
	}
	return EXIT_SUCCESS;
}
			
