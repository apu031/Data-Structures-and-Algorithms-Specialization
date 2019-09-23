# Uses python3

import sys
import queue


def distance(adj, s, t):
    # write your code here
    # Initialize all the dist to infinity
    dist = [float('inf')] * len(adj)
    # Initialize s to 0
    dist[s] = 0
    # Create a queue of size same as the number of vertices
    q = queue.Queue(maxsize=len(adj))
    # Store the source in S
    q.put(s)

    # Checking if queue is empty
    while not q.empty():
        # Getting vertices out from the queue
        u = q.get()

        # Checking the edges connected with u
        for v in adj[u]:
            # If distance to v is infinity, then enqueue v
            # and calculate the distance to v from u
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[u] + 1

    # Check the target distance
    if dist[t] == float('inf'):
        # If infinity, then t is not reachable from s
        return -1
    else:
        # Otherwise return distance for t
        return dist[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
