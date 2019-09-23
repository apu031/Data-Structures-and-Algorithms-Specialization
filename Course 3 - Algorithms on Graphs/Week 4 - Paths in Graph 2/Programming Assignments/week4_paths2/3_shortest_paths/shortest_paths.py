#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
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
    dist, prev = bellman_ford(adj, cost, s)
    # print(distance)
    # Bellman-ford promises shortest distance if no negative weight cycle exists.
    # If we get a shorter path on nth iteration, then there is a negative weight cycle
    # We run again n - 1 times so that we can update all the possible edges.
    for n in range(len(adj) - 1):
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                if dist[adj[i][j]] > dist[i] + cost[i][j]:
                    dist[adj[i][j]] = -float('inf')
                    shortest[adj[i][j]] = 0

    # Checking the reachablity from s
    # If a vertex is reachable, its prev is definitely not -1.
    for i in range(len(prev)):
        if prev[i] != -1:
            reachable[i] = 1
    # Updating distance array with dist
    for i in range(len(dist)):
            distance[i] = dist[i]


def bellman_ford(adj, cost, s):
    """
    This algorithm finds the shortest path from s to any other node.
    This definition runs n-1 times without thinking of finding negative cycles,
    but possible distance from s. Therefore, we do not take unconnected clusters
    into consideration like we did in negative_cycle detection. Here we are only
    considering whether all the vertices are reachable from s after n-1 edge
    relaxations. If yes, then what are the distance after n-1 relaxations.
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
    dist[s] = 0
    prev[s] = s
    # Relax each edge for |V| - 1 times
    # because each vertex can be connected to at most |V|-1 edges
    for n in range(len(adj) - 1):
        # Relax all the edges
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                # If distance for u=adj[u] is still infinity, then turn it 0
                # This is required to handle unconnected clusters in the graph
                # if dist[i] == float('inf'):
                #     dist[i] = 0
                # If the distance for v=adj[i][j] is more than
                # distance upto u=i and the addition of the weight from u to v
                if dist[adj[i][j]] > dist[i] + cost[i][j]:
                    # Update the distance for v
                    dist[adj[i][j]] = dist[i] + cost[i][j]
                    # Store u as a predecessor of v
                    prev[adj[i][j]] = i
    return dist, prev


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
    s = data[0]
    s -= 1
    # s = 3
    # n, m = 6, 7
    # # Graph with unconnected clusters
    # adj = [[1], [2], [0], [1, 5], [3], [4]]
    # cost = [[2], [3], [1], [3, -2], [1], [-5]]
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        # print(distance[x])
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

