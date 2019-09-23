# Uses python3

import sys


def reach(adj, x, y):
    """
    This definition checks if there is a path from x to y.
    However, it does not consider any loop implementation.
    :param adj: Adjacency List
    :param x:   Source
    :param y:   Target
    :return:    1, if there is a path from x to y. Otherwise, 0.
    """
    # write your code here
    # Creating a memoize for visited vertices, and initializing it to False
    visited = [False] * len(adj)

    # Start exploring vertex x
    explore(adj, visited, x)

    # If y can be reachable from x, it should be already visited
    # If y is reachable return 1, or return 0
    if not visited[y]:
        return 0
    else:
        return 1


def explore(adj, visited, u):
    # Mark the vertex v as visited
    visited[u] = True

    # Checking every edges from u
    for v in adj[u]:
        # If v has not been visited, explore v.
        if not visited[v]:
            explore(adj, visited, v)


if __name__ == '__main__':
    input = sys.stdin.read()  # To terminate input use Ctlr+D = EOF
    data = list(map(int, input.split()))  # Storing each input as a list element
    n, m = data[0:2]  # Collecting n = # of vertices, m = # of edges
    data = data[2:]  # The edges
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))  # Storing edges as tuples in a list
    x, y = data[2 * m:]  # The last line indicates the x = source, y = sink
    adj = [[] for _ in range(n)]  # Creating adjacency list
    x, y = x - 1, y - 1  # Reducing each vertices to match the 0th index
    for (a, b) in edges:  # Creating adjacency list
        adj[a - 1].append(b - 1)  # a-1, and b-1 to match the 0th index
        adj[b - 1].append(a - 1)  # Adding twice because undirected graph
    print(reach(adj, x, y))
