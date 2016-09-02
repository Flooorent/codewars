#!/usr/bin/python

def find_shortest_path(grid, start_node, end_node):
    """Breadth-first search seems to work well in this situation."""
    if not grid:
        return []

    N = len(grid)
    M = len(grid[0])

    nodes = {}
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            nodes[grid[i][j]] = None

    def reachable_nodes(node):
        x = node.position.x
        y = node.position.y
        all_coords = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        possible_coords = filter(lambda (i, j): 0 <= i and i < N and 0 <= j and j < M, all_coords)
        possible_nodes = [grid[i][j] for (i, j) in possible_coords]
        candidates = filter(lambda node: node.passable, possible_nodes)
        return candidates

    buff = [start_node]
    level = 0

    # BFS here
    while buff:
        temp = []
        for node in buff:
            if (not nodes[node]) or (nodes[node] > level):
                nodes[node] = level
                temp.extend(reachable_nodes(node))
        buff = temp
        level += 1

    path = [end_node]

    def find_path(node, value):
        """
        Here we take advantage of the fact that each node in the shortest 
        path is one move apart from its neighbour.
        """
        if (not value) or (value < 0): # not value is here simply to handle the 1x1 grid case
            return
        elif value == 0:
            path.append(node)
            return
        if (node == start_node) or (value == 1):
            path.append(start_node)
        else:
            prev_node = filter(lambda x: nodes[x] == (value-1), reachable_nodes(node))[0]
            path.append(prev_node)
            find_path(prev_node, value-1)


    find_path(end_node, nodes[end_node])

    return list(reversed(path))
