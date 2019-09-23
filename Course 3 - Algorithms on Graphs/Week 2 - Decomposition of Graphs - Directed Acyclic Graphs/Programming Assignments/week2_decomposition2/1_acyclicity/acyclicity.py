# Uses python3

import sys


def acyclic(adj):
    """
    This definition finds if there is a cycle in a graph.
    :param adj: The adjacency list
    :return: 1, if there is a cycle. Otherwise, 0.
    """

    # Creating a memoize for visited vertices, and initializing it to False
    visited = [False] * len(adj)
    # Having an ancestor stack to keep track of the starting vertex
    ancestor_stack = [False] * len(adj)

    # Start exploring vertex v from adj
    for v in range(len(adj)):
        # If v has not been visited, check cycle for v.
        if not visited[v]:
            # If cycle exists, return 1
            if cycle_check(adj, ancestor_stack, visited, v):
                return 1
        else:
            # If v has been visited, then check for v in the ancestor stack
            if ancestor_stack[v]:
                # If v is in ancestor stack, return 1
                return 1
    return 0


def cycle_check(adj, ancestor_stack, visited, u):
    # Mark the vertex v as visited
    visited[u] = True
    ancestor_stack[u] = True
    # Checking every edges from u
    for v in adj[u]:
        # If v has not been visited, check cycle for v.
        if not visited[v]:
            # If cycle exists, return 1
            if cycle_check(adj, ancestor_stack, visited, v):
                return 1
        else:
            # If v has been visited, then check for v in the ancestor stack
            if ancestor_stack[v]:
                # If v is in ancestor stack, return 1
                return 1
    # Remove the ancestor vertex from the stack, before
    # exiting cycleCheck without finding any cycle, so
    # that the next iterations can be performed without
    # falsely considering a vertex as an ancestor.
    ancestor_stack[u] = False


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
