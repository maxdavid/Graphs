from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for member in ancestors:
        graph.add_vertex(member[0])
        graph.add_vertex(member[1])

    for vertex in ancestors:
        graph.add_edge(*vertex)

    max_path = []
    for vertex in ancestors:
        path = graph.dfs(vertex[0], starting_node)
        if path is not None and len(path) > len(max_path):
            max_path = path.copy()

    if len(max_path) <= 1:
        return -1
    return max_path[0]
