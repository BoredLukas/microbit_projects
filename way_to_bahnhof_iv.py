graph = {
    "ksr": {"sek": 1},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7},
    "hafenstr": {"bahnhof": 6},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
}

visited = ["ksr"]
ways_to_bahnhof = {}
candidates = ["ksr"]

while candidates:
    node = candidates.pop(0)
    if node == "bahnhof":
        print("way found")
    else:
        for ways in graph[node]:
            candidates.append(ways)
        visited.append(node)
        parent = node
        ways_to_bahnhof[parent]=graph[parent][node]
        print(ways_to_bahnhof)
        print(candidates)
        print(visited)

