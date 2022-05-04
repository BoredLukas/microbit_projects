graph = {
    "ksr": {"sek": 1},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7},
    "hafenstr": {"bahnhof": 6},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
}

START = "ksr"
END = "bahnhof"
SEARCH = True
way_to_bahnhof = ["ksr"]

def connection_check(graph, n1, n2):
    x1 = n2 in graph[n1]
    return x1

def find_way(given_node):
    for node in graph[given_node]:
        way_to_bahnhof.append(node)
        return node

node = find_way(START)
while SEARCH:
    node = find_way(node)
    if node == "bahnhof":
        SEARCH = False
        print(way_to_bahnhof)
    for nodes in way_to_bahnhof:
        if nodes == node:
            pass