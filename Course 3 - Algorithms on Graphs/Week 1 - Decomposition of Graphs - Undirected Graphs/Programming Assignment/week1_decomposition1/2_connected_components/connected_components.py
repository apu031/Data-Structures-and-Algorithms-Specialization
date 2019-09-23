# Uses python3

import sys


def number_of_components(adj):
    """
    This definition finds the number of connected components.
    :param adj: The adjacency list
    :return: The total number of connected components.
    """
    # Initializing number of connected components to 0.
    result = 0
    # write your code here
    # Creating a memoize for visited vertices, and initializing it to False
    visited = [False] * len(adj)

    # Start exploring vertex v from adj
    for v in range(len(adj)):

        if not visited[v]:
            explore(adj, visited, v)
            # After exploring each vertex from the adjacent list,
            # add 1 to the number of connected components
            result += 1
    return result


def explore(adj, visited, u):
    # Mark the vertex v as visited
    visited[u] = True

    # Checking every edges from u
    for v in adj[u]:
        # If v has not been visited, explore v.
        if not visited[v]:
            explore(adj, visited, v)


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
    print(number_of_components(adj))
