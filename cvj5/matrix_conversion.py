from graph_helpers import check_graph, get_edge_counter


def get_vertices(neighborhood_list):
    vertices = [vertex for vertex in neighborhood_list.keys()]
    return vertices


def make_neighborhood_matrix(neighborhood_list):
    neighborhood_matrix = []
    vertices = get_vertices(neighborhood_list)

    for i in range(len(neighborhood_list)):
        neighborhood_matrix.append([])
        for j in range(len(neighborhood_list)):
            neighborhood_matrix[i].append(0)

    try:
        for i in neighborhood_list:
            for j in neighborhood_list[i]:
                if j[0] in vertices:
                    column = vertices.index(i)
                    row = vertices.index(j[0])
                    neighborhood_matrix[column][row] = j[1]
    except:
        for i in neighborhood_list:
            for j in neighborhood_list[i]:
                if j in vertices:
                    column = vertices.index(i)
                    row = vertices.index(j)
                    neighborhood_matrix[column][row] = 1

    print("\n Neighborhood matrix:")
    print_matrix(neighborhood_matrix)

    return neighborhood_matrix


def make_incidence_matrix(neighborhood_list, arcs, edges_file):
    incidence_matrix = []
    column = 0

    edges = get_edge_counter(neighborhood_list)

    for i in range(len(neighborhood_list)):
        incidence_matrix.append([])
        for j in range(edges):
            incidence_matrix[i].append(0)

    is_arc, is_edge, directed, difficulty = check_graph(arcs, edges_file)

    if directed:
        if difficulty:
            for _ in neighborhood_list:
                for j in arcs:
                    if column > edges - 1:
                        break
                    row1 = int(j[0]) - 1
                    row2 = int(j[1]) - 1
                    incidence_matrix[row1][column] = int(j[2])
                    incidence_matrix[row2][column] = int(j[2])
                    column += 1
        else:
            for _ in neighborhood_list:
                for j in arcs:
                    if column > edges - 1:
                        break
                    row1 = int(j[0]) - 1
                    row2 = int(j[1]) - 1
                    incidence_matrix[row1][column] = -1
                    incidence_matrix[row2][column] = -1
                    column += 1
    else:
        if difficulty:
            for _ in neighborhood_list:
                for j in edges_file:
                    if column > edges - 1:
                        break
                    row1 = int(j[0]) - 1
                    row2 = int(j[1]) - 1
                    incidence_matrix[row1][column] = int(j[2])
                    incidence_matrix[row2][column] = int(j[2])
                    column += 1
        else:
            for _ in neighborhood_list:
                for j in edges_file:
                    if column > edges - 1:
                        break
                    row1 = int(j[0]) - 1
                    row2 = int(j[1]) - 1
                    incidence_matrix[row1][column] = 1
                    incidence_matrix[row2][column] = 1
                    column += 1

    print("Incidence matrix:")
    print_matrix(incidence_matrix)

    return incidence_matrix


def num_string_array(num, vertices):
    string = ""

    for i in range(len(vertices)):
        if num == vertices[i][0]:
            string = vertices[i][1]
            return string


def make_neighborhood_list(vertices, arc, edges):
    neighborhood_list = {}
    temp_sort = []

    ia_arc, is_edge, directed, difficulty = check_graph(arc, edges)

    if ia_arc:
        for vertex in range(len(vertices)):
            for row in arc:
                if difficulty:
                    if row[0] in vertices[vertex][0]:
                        name = num_string_array(row[1], vertices)
                        name_diff = [name, row[2]]
                        temp_sort.append(name_diff)
                    if not directed:  # nece ici u drugom smjeru jer je usmjeren
                        if row[1] in vertices[vertex][0]:
                            name = num_string_array(row[0], vertices)
                            name_diff = [name, row[2]]
                            temp_sort.append(name_diff)
                else:
                    if row[0] in vertices[vertex][0]:
                        name = num_string_array(row[1], vertices)
                        temp_sort.append(name)
                    if not directed:
                        if row[1] in vertices[vertex][0]:
                            name = num_string_array(row[0], vertices)
                            temp_sort.append(name)

            neighborhood_list[vertices[vertex][1]] = temp_sort
            temp_sort = []

    if is_edge:
        for vertex in range(len(vertices)):
            for edge in edges:
                if difficulty:
                    if edge[0] in vertices[vertex][0]:
                        name = num_string_array(edge[1], vertices)
                        name_diff = [name, edge[2]]
                        temp_sort.append(name_diff)
                    if edge[1] in vertices[vertex][0]:
                        name = num_string_array(edge[0], vertices)
                        name_diff = [name, edge[2]]
                        temp_sort.append(name_diff)
                else:
                    if len(edge) > 0:
                        if edge[0] in vertices[vertex][0]:
                            name = num_string_array(edge[1], vertices)
                            temp_sort.append(name)
                        elif edge[1] in vertices[vertex][0]:
                            name = num_string_array(edge[0], vertices)
                            temp_sort.append(name)

            neighborhood_list[vertices[vertex][1]] = temp_sort
            temp_sort = []

    print("Graph neighborhood list:")
    for i in vertices:
        print(i[1], " - ", neighborhood_list[i[1]])

    return neighborhood_list


def print_matrix(data):
    for i in range(len(data)):
        print(data[i])
