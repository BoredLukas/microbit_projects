graph = {
    "ksr": {"sek": 1},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7},
    "hafenstr": {"bahnhof": 6},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
}

way_to_bahnhof = [["ksr"]]
visited = ["ksr"]

def connection_check(graph, n1, n2):
    x1 = n2 in graph[n1]
    return x1

def find_way(graph, way_to_bahnhof, visited):
    def node_append(given_node):
        for node in graph[given_node]:
            way_to_bahnhof[0].append(node)
            return node

    START = "ksr"
    END = "bahnhof"
    SEARCH = True

    node = node_append(START)
    visited.append(node)
    while SEARCH:
        last_node = node
        node = node_append(node)
        visited.append(node) 
        if node == "bahnhof":
            SEARCH = False
            print(way_to_bahnhof)
            print(visited)
    return way_to_bahnhof

cycles = find_way(graph, way_to_bahnhof, visited)
print(cycles)