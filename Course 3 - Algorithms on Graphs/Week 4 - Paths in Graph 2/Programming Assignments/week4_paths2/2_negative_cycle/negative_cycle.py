# Uses python3

import sys


def negative_cycle(adj, cost):
    """
    This definition detects the presence of a negative weight cycle in a graph.
    Step 1: It finds the shortest path using Bellman-Ford algorithm with
            |V|-1 times edge relaxation. If a graph does not contain a negative
            weight cycle, then Bellman-Ford returns shortest distance from source
            to any other vertices.
            Note - There can be at most |V|-1 edges from a vertex, given no cycle.
    Step 2: Run the Vth relaxation. If there is a negative cycle, we get shorter path.
    :param adj: The adjacency list
    :param cost: The list of weight that corresponds to the adjacency list
    :return: 1, if there is a negative weight cycle, otherwise 0.
    """
    # write your code here
    # bellman_ford returns the shortest distance after n-1 iteration
    dist, prev, vertex = nth_bellman_ford(adj, cost, 0)

    # Bellman-ford promises shortest distance if no negative weight cycle exists.
    # If we get a shorter path on nth iteration, then there is a negative weight cycle
    # for i in range(len(adj)):
    #     for j in range(len(adj[i])):
    #         if dist[adj[i][j]] > dist[i] + cost[i][j]:
    #             return 1

    if vertex == -1:
        return 0
    else:
        for i in range(len(adj)):
            vertex = prev[vertex]
        v = vertex
        while True:
            v = prev[v]
            if v == vertex:
                return 1


    # return 0


def nth_bellman_ford(adj, cost, s):
    """
    This algorithm finds the shortest path from s to any other node.
    :param adj: The adjacency list
    :param cost: The list of weight that corresponds to the adjacency list
    :param s: Source
    :return: dist = The list of distances from s to other vertices
             prev = The list of ancestors
    """
    # Initialize distance for all vertices to infinity
    dist = [float('inf')] * len(adj)
    # Initialize ancestor for all vertices to the vertex itself
    prev = [-1] * len(adj)
    # Set the distance for the source to 0
    # dist[s] = 0
    vertex = -1
    # Relax each edge for |V| - 1 times
    # because each vertex can be connected to at most |V|-1 edges
    for n in range(len(adj)):
        vertex = -1
        # Relax all the edges
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                # If distance for u=adj[u] is still infinity, then turn it 0
                # This is required to handle unconnected clusters in the graph
                if dist[i] == float('inf'):
                    dist[i] = 0
                # If the distance for v=adj[i][j] is more than
                # distance upto u=i and the addition of the weight from u to v
                if dist[adj[i][j]] > dist[i] + cost[i][j]:
                    # Update the distance for v
                    dist[adj[i][j]] = dist[i] + cost[i][j]
                    # Store u as a predecessor of v
                    prev[adj[i][j]] = i
                    vertex = adj[i][j]
    return dist, prev, vertex


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

    # Negative cycle, return 1
    # adj = [[1], [2], [0], [0]]
    # cost = [[-5], [2], [1], [2]]

    # Positive cycle, return 0
    # adj = [[1], [2], [0], [0]]
    # cost = [[5], [2], [1], [2]]

    # No cycle, return 0
    # adj = [[1, 2], [2], [], [0]]
    # cost = [[-5, 1], [2], [], [2]]

    # Graph with unconnected clusters
    # adj = [[1], [2], [0], [1, 5], [3], [4]]
    # cost = [[2], [3], [1], [3, -2], [1], [-5]]
    print(negative_cycle(adj, cost))
