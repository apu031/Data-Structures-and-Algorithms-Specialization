# Uses python3

import sys
import queue


def bipartite(adj):
    """
    This definition finds if a graph is bipartite by assigning different colors to
    each vertex of an edge. If no edge contains similar colored vertices on both ends,
    then the graph is a bipartite graph.
    Algorithm:
    1. Initialize all the vertices with color -1(black).
    2. Initialize source color as 1.
    3. Add the source to the priority queue.
    4. If the queue is not empty, pop the value u.
        5. Check all the edges from u to v.
            6. If color[v] == -1, then color[v] = 1 - color[u]
            7. If color[v] == color[u], then two vertices of a single edge has the same color,
            so return 0.
    7. return 1 to indicate the graph is bipartite.
    :param adj: The adjacency list
    :return: 1 if the graph is bipartite, otherwise 0.
    """
    # write your code here
    # Initialize all the vertices color as -1
    color_graph = [-1] * len(adj)
    # Assign 1 for source vertex color
    color_graph[0] = 1
    # Initialize the priority queue
    q = queue.Queue(maxsize=len(adj))
    # Put the source inside the priority queue
    q.put(0)
    # While queue is not empty
    while not q.empty():
        # Pop the vertex from the queue (FIFO)
        u = q.get()
        # Check all the edges of the vertex u
        for v in adj[u]:
            # If the vertex v from u has not been visited yet, it color should be -1,
            # In that case, assign new color to v by doing 1 - color[u]
            # Push v to the queue
            if color_graph[v] == -1:
                color_graph[v] = 1 - color_graph[u]
                q.put(v)
            # If the vertex v has already been discovered, then it should have a different
            # value than -1. Check if the value is same as color[u]. In that case, two vertices
            # from the same edge have the same color. Therefore, the graph is not bipartite.
            elif color_graph[v] == color_graph[u]:
                return 0
    # If all the vertices for all the edges are colored differently, then the graph is bipartite.
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
