graph = {
    "ksr": {"sek": 1, "weitenzelgstr": 1},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7},
    "hafenstr": {"bahnhof": 6},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
    "weitenzelgstr": {},
}

def connection_check(graph, n1, n2):
    x1 = "bahnhofstr" in graph["sek"]
    return x1

def way_to_bahnhof(graph):
    for ways in graph["ksr"]:
        x = graph["ksr"]
        print(x)
        
print(connection_check(graph, 1, 3))
way_to_bahnhof(graph)