def get_vertex_count(neighborhood_list):
    return len(neighborhood_list.keys())


def get_edge_counter(neighborhood_list):
    counter = 0
    for i in neighborhood_list:
        for _ in neighborhood_list[i]:
            counter += 1

    return counter


def get_longest_edge(neighborhood_list):
    Max = 0
    max_name = []

    for i in neighborhood_list:
        if len(neighborhood_list[i]) > Max:
            Max = len(neighborhood_list[i])
            max_name = []
        if len(neighborhood_list[i]) == Max:
            max_name.append(i)

    return max_name


def get_degree_vertex(neighborhood_list):
    degree = {}

    for i in neighborhood_list:
        counter = 0
        for j in neighborhood_list[i]:
            counter += 1
        degree[i] = counter

    return degree


def is_euler(degree_vertex):
    for i in degree_vertex.values():
        if i % 2 != 0:
            return False

    return True


def check_graph(arc, edges):
    directed = False
    difficulty = False
    is_arc = False
    is_edge = False

    if len(arc) > 1:
        is_arc = True
        directed = True
        if len(arc[0]) > 2:
            difficulty = True
    else:
        print("Arc doesn't exist")

    if len(edges) > 0:
        is_edge = True
        if len(edges[0]) > 2:
            difficulty = True
    else:
        print("Edges doesn't exist")

    if directed:
        print("Graph is directed")
    else:
        print("Graph isn't directed")

    if difficulty:
        print("Graph is difficult")
    else:
        print("Graph isn't difficult")

    return is_arc, is_edge, directed, difficulty
