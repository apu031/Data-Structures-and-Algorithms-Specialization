# Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    """
    This definition finds the shortest distance from s to t.
    :param adj: The adjacency list
    :param cost: The list of edge weights the corresponds to adj
    :param s: Source
    :param t: Target
    :return: Shortest distance from s to t. If t is unreachable, then -1.
    """
    # write your code here
    for i in range(len(cost)):
        for weight in cost[i]:
            if weight <= 0:
                return -1
    # Initialize the distance to infinity
    dist = [float('inf')] * len(adj)
    # Initialize ancestor vertex to None
    prev = [0] * len(adj)
    # Turn the source distance to 0
    dist[s] = 0
    # Initialize a priority queue
    pq = queue.PriorityQueue()
    # Insert all the vertices as distance-vertex pairs
    createPriorityQueue(dist, pq)
    # While the queue is not empty,
    while not pq.empty():
        # Pop the item with the list distance value
        (w, u) = pq.get()  # w = distance, u = vertex
        # Iterate over all the edges going out from u
        for i in range(len(adj[u])):
            # If distance of v = adj[u][i] is more than distance upto u and the addition of edge weight
            if dist[adj[u][i]] > dist[u] + cost[u][i]:
                # Then update distance for v
                dist[adj[u][i]] = dist[u] + cost[u][i]
                # Store u as an ancestor of v
                prev[adj[u][i]] = u
                # Update the distance-vertex for v in the priority queue
                changePriority(pq, adj[u][i], dist[adj[u][i]])

    # If distance t is never reached, return -1
    if dist[t] == float('inf'):
        return -1
    else:
        # Else return the distance from s to t
        return dist[t]


def createPriorityQueue(dist, pq):
    """
    This definition populates the priority queue with (distance, vertex) pairs
    :param dist: The distance list
    :param pq: The priority queue
    :return: None
    """
    for i in range(len(dist)):
        pq.put((dist[i], i))


def changePriority(pq, v, new_dist):
    """
    This definition updates the distance for a vertex in the priority queue.
    :param pq: The priority queue
    :param v: The vertex that needs to be updated
    :param new_dist: The new distance to reach vertex, v
    :return: None
    """
    updated = False
    for (dist, vertex) in pq.queue:
        if vertex == v:
            # Upon finding the vertex, remove the previous (distance, vertex) pair
            pq.queue.remove((dist, vertex))
            # Insert the new (distance, vertex) pair
            pq.put((new_dist, v))
            updated = True
            break
    # If the vertex is not present, then just add the weight-vertex
    if not updated:
        pq.put((new_dist, v))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
