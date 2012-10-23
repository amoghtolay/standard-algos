/*
 * For O(logn), competition of Tower Research
 * Implementation of Bellman Ford on a graph expressed as an array of
 * edges which contain the start and end vertices along with the weight
 */

#include <stdlib.h>
#include <stdio.h>

#define INF 10000000

struct edge
{
	int source;
	int dest;
	int weight;
};

int main()
{
	int T;
	scanf("%d",&T);
	int source,target;
	for (int i=0; i<T; i++)
	{
		int numVert, numEdges;
		scanf("%d %d", &numVert, &numEdges);
		int vertexList[numVert];
		edge edgeList[numEdges];
		
		for (int i=0; i<numEdges; i++)
			scanf("%d %d %d", &edgeList[i].source, &edgeList[i].dest, &edgeList[i].weight);
		
		// Graph complete
		int Q;
		scanf("%d",&Q);
		
		for (int j=0; j<Q; j++)
		{
			scanf("%d %d", &source, &target);
			/*
			 * Bellmann code here
			 */
			for (int i=0; i<numVert; i++)
				vertexList[i] = INF;

			vertexList[source] = 0;
			
			// Relax edges
			for (int i=0; i<numVert; i++)
				for (int j=0; j<numEdges; j++) // uv is the edge from u to v
				{
					if ( vertexList[edgeList[j].source] != INF && vertexList[edgeList[j].source] + edgeList[j].weight < vertexList[edgeList[j].dest] )
						vertexList[edgeList[j].dest] = vertexList[edgeList[j].source] + edgeList[j].weight;
				}
			// Ends here
			printf("%d\n", vertexList[target]);
		}
	}
	return EXIT_SUCCESS;
}
