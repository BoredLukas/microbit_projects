from tracemalloc import start


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
start = "ksr"
candidates = [start]

while candidates:
    node = candidates.pop(0)
    if node == "bahnhof":
        print("way found")
    else:
        for ways in graph[start]:
            candidates.append(ways)
        visited.append(start)
        old = start
        start = candidates.pop(0)
        ways_to_bahnhof[old]=graph[start]
        print(ways_to_bahnhof)
        print(candidates)
        print(visited)

