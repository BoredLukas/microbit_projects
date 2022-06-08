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
parent = "ksr"

while candidates:
    node = candidates.pop(0)
    if node == "bahnhof":
        print("way found")
    elif node in visited:
        continue
    elif not node in graph:
        
    else:
        for ways in graph[node]:
            candidates.append(candidates)
        visited.append(node)
        ways_to_bahnhof[parent]=graph[parent][node]
        parent = node
        print(ways_to_bahnhof)
        print(candidates)
        print(visited)

