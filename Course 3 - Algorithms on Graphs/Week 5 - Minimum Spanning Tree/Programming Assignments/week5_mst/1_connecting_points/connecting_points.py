# Uses python3
import bisect
import math
import sys


def minimum_distance(x, y):
    result = 0.
    # write your code here
    # Create vertices from the points
    vertices = create_vertex(x, y)

    # Calculate all the possible distances and store it in sorted manner
    edges = create_sorted_undirected_edge(vertices)

    # Create sets from vertices
    set_list = create_set(vertices)

    # For every edge, check if the pair of vertices (u,v) is a subset of sets stored in setList.
    # If it is not, then unionize the sets containing u, and v. Remove the sets that has
    # been used for unionizing from the setList.
    for edge in edges:
        # If setList has only 1 element, means all the vertices has been connected.
        # So break the loop from further futile checking
        if len(set_list) == 1:
            break
        # If (u, v) is not a subset of any set stored in setList,
        # then unionize the sets containing u, and v.
        # Remove the sets that has been used for unionizing from the setList.
        # Add the newly unionized set to the setList
        if not find_subset(set_list, edge[1]):
            update_set(set_list, edge[1])
            # Add the edge distance to the overall result to get the total shortest distance.
            result += edge[0]

    return result


def create_vertex(x, y):
    """
    This definition creates the vertices from two lists of x and y coordinates.
    :param x: The list of x coordinates
    :param y: The list of y coordinates
    :return: The list of vertices
    """
    vertices = []
    for i in range(len(x)):
        vertices.append([x[i], y[i]])
    return vertices


def create_set(vertices):
    """
    This definition creates the sequential set of vertices from a given list of vertices.
    :param vertices: The list of vertices.
    :return: A list containing all the vertices as sets.
    """
    set_list = []
    for i in range(len(vertices)):
        set_list.append({i})
    return set_list


def create_sorted_undirected_edge(vertices):
    """
    This definition calculates all the possible edge distance for an undirected graph.
    :param vertices: The list of vertices
    :return: The list of edge distance where each element is [distance, (u, v)]
    """
    edges = []
    # Run the outter loop from 0 to |V|-1
    for i in range(len(vertices) - 1):
        # Run the inner loop from i to |V|
        for j in range(i + 1, len(vertices)):
            # Calculate the distance between the two vertices
            distance = get_distance(vertices[i], vertices[j])
            # If the vertices are not the same, then add it to the list in sorted fashion
            if distance > 0:
                bisect.insort(edges, [distance, {i, j}])
    return edges


def find_subset(set_list, sub):
    """
    This definition finds if a pair of vertices {u, v} is already a subset of any set present in setList.
    :param set_list: The list of sets.
    :param sub: The pair of vertices {u, v}
    :return: True, if {u, v} is a subset of any set. Otherwise, False
    """
    for s in set_list:
        if sub.issubset(s):
            return True
    return False


def update_set(set_list, sub):
    """
    This definition updates the setList with the new edge that has a pair of vertices {u, v}
    :param set_list: The list of sets
    :param sub: The pair of vertices {u, v}
    :return: None
    """
    s1 = set()
    s2 = set()
    sub = list(sub)

    for i in range(len(set_list)):
        # If u is present in any of the set, pop the set out of the setList.
        if sub[0] in set_list[i]:
            s1 = set_list.pop(i)
            break

    for j in range(len(set_list)):
        # If v is present in any of the set, pop the set out of the setList
        if sub[1] in set_list[j]:
            s2 = set_list.pop(j)
            break
    # Unionize s1 and s2 that contain u and v respectively.
    # Add the unionized set to the setList
    set_list.append(s1.union(s2))


def get_distance(u, v):
    """
    This definition finds the distance between two vertices (u, v).
    :param u: The first vertex where u[0] = x1, and u[1] = y1
    :param v: The second vertex where v[0] = x2, and v[1] = y2
    :return: The distance between u and v
    """
    return math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    # x = [0, 0, 1, 3, 3]
    # y = [0, 2, 1, 0, 2]
    print("{0:.9f}".format(minimum_distance(x, y)))
