def find_path(graph, node=None, end=None, visited=set()):

    if node == None:
        node = next(iter(graph))
    if end == None:
        end = list(graph)[-1]
     
    if node in visited:
        return False
       
    if node == end:
        return [end]
     
    visited.add(node)
     
    edges = graph[node]
    for neighbor in edges:
        path = find_path(graph, neighbor, end, visited)
        if path:
            return [node] + path
    return False

def cycle_search(graph, node, path=[]):
    for node in path:
        index = path.index(node)
        cycle = path[index:]
        print(cycle)
        return

    path.append(node)
    for neighbour in graph[node]:
        length = len(path)
        cycle_search(graph, neighbour, path)
        path = path[:length]

graph = {
    "ksr": {"sek": 1, "weitenzelgstr": 1},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7},
    "bahnhofstr": {"ksr": 1},
    "hafenstr": {"bahnhof": 6},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
}

cycle_search(graph, "ksr")