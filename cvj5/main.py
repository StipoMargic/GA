from graph_helpers import get_degree_vertex, get_vertex_count, get_edge_counter, get_longest_edge, is_euler, check_graph
from matrix_conversion import make_incidence_matrix, make_neighborhood_matrix, get_vertices, make_neighborhood_list
import sys
import random

filter = ['"', ',', '\n']


def clean_line(string):
    for i in filter:
        string = string.replace(i, '')
    return string


def read_graph():
    vertices = []
    arcs = []
    edges = []
    is_ver = False
    is_arc = False
    is_edge = False

    with open(sys.argv[1]) as file:
        for line in file:
            line = clean_line(line)

            if is_ver and line.lower() not in "*arcs":
                vertices.append(line.split())

            if "*vertices" in line.lower():
                is_ver = True

            if is_arc and line.lower() not in "*edges":
                arcs.append(line.split())

            if "*arcs" in line.lower():
                is_arc = True
                is_ver = False

            if is_edge:
                edges.append(line.split())

            if "*edges" in line.lower():
                is_edge = True
                is_ver = False
                is_arc = False

    print("Vert: ", vertices, "Arcs: ", arcs, "Edges: ", edges)
    return vertices, arcs, edges


vertices, arc, edges = read_graph()
neighborhood_list = make_neighborhood_list(vertices, arc, edges)
# incidence_matrix = make_incidence_matrix(neighborhood_list, arc, edges)
# neighborhood_matrix = make_neighborhood_matrix(neighborhood_list)
#
# print("Number of vertices: ", get_vertex_count(neighborhood_list))
# print("Number of edges", get_edge_counter(neighborhood_list))
print("Degree of vertices: ", get_degree_vertex(neighborhood_list))
# print("Longest edge: ", get_longest_edge(neighborhood_list))

if is_euler(get_degree_vertex(neighborhood_list)):
    print("Graph is euler")
else:
    print("Graph is not euler")

ia_arc, is_edge, directed, difficulty = check_graph(arc, edges)


def euler(n_list):
    start = random.choice(list(n_list.keys()))

    n_exit = get_degree_vertex(n_list)

    path = searchPath(start, n_exit, n_list)

    print(path)


def searchPath(current, n_exit, n_list):
    path = []
    while n_exit[current] != 0:
        next_n = random_neighbor(current, n_list)
        n_exit[current] -= 1
        n_list[current].remove(next_n)
        path = searchPath(next_n, n_exit, n_list)

    path[:0] = [current]
    return path


def random_neighbor(current, n_list):
    return random.choice(list(n_list[current]))


euler(neighborhood_list)
