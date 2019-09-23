# Uses python3

import sys


def dfs(adj, used, order, x):
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
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
