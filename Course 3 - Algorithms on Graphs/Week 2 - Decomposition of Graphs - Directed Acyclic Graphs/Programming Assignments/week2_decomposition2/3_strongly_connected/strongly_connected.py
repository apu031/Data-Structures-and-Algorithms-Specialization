# Uses python3

import sys

sys.setrecursionlimit(200000)  # Set recursion limit to avoid overflow of c stack


def number_of_strongly_connected_components(adj):
    """
    This definition finds the number of strongly connected components in a graph.
    :param adj: The adjacency list
    :return: The number of strongly connected components.
    """
    result = 0
    # write your code here
    # Find the reverse graph
    trans_graph = transpose_graph(adj)
    # Find the topological order of the reverse graph,
    # To find the sink vertex of the original graph.
    trans_order = toposort(trans_graph)

    # Creating a memoize for visited vertices, and initializing it to False
    visited = [False] * len(adj)
    order = []
    for v in trans_order:
        if not visited[v]:
            # If v is not visited, run dfs from v, and add to the strongly connected component
            dfs(adj, visited, order, v)
            result += 1
    return result


def transpose_graph(adj):
    """
    This function finds the reverse or transpose of an adjacency list.
    :param adj: The adjacency list
    :return: The transposed adjacency list
    """
    trans_adj = [[] for _ in range(len(adj))]

    for i in range(len(adj)):
        for j in adj[i]:
            trans_adj[j].append(i)

    return trans_adj


def dfs(adj, used, order, x):
    """
    This definition traverse the graph as a depth fast search,
    and store the vertices with increasing postorder value
    :param adj: The adjacency list
    :param used: The visited vertex list
    :param order: The list of vertices with increasing postorder value
    :param x: The source vertex or the vertex from which dfs starts
    :return: None
    """
    # write your code here
    # Mark as visited
    used[x] = 1
    for v in adj[x]:
        if not used[v]:
            # If not visited, run dfs
            dfs(adj, used, order, v)
    # When no more recursion, add to the order list
    order.append(x)


def toposort(adj):
    """
    This definition finds the topological order of the vertices in a directed acyclic graph.
    :param adj: The adjacency list
    :return: The list of vertices in decreasing postorder value
    """
    # Memoize for visited vertex
    used = [0] * len(adj)
    order = []
    # write your code here
    # Traverse through each vertex
    for i in range(len(adj)):
        if not used[i]:
            # If not visited, run dfs
            dfs(adj, used, order, i)

    # Reverse the order list to show in descending order
    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
