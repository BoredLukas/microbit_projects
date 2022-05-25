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
    def node_append_first_list(given_node,list):
        for node in graph[given_node]:
            list[0].append(node)
            return node

    def find_other_ways():
        pass

    START = "ksr"
    END = "bahnhof"
    SEARCH = True

    node = node_append_first_list(START, way_to_bahnhof)
    visited.append(node)
    while SEARCH:
        last_node = node
        node = node_append_first_list(node, way_to_bahnhof)
        # index = way_to_bahnhof.index(last_node)
        visited.append(node) 
        if node == END:
            SEARCH = False
            print(way_to_bahnhof)
            print(visited)
            # print(index)
    return way_to_bahnhof

cycles = find_way(graph, way_to_bahnhof, visited)
print(cycles)