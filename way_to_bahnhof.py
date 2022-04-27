graph = {
    "ksr": {
        1: {"sek": 1}, 
        2: {"weitenzelgstr": 1}
    },
    "sek": {
        1: {"bahnhofstr": 3}, 
        2: {"hafenstr": 5}, 
        3: {"zelgstr": 7}
    },
    "bahnhofstr": {
        1: {"bahnhof": 7}
    },
    "hafenstr": {
        1: {"bahnhof": 6}
    },
    "zelgstr": {
        1: {"bahnhof": 5}
    },
    "bahnhof": {},
    "weitenzelgstr": {},
}

def connection_check(graph, n1, n2):
    x1 = "bahnhofstr" in graph["sek"]
    return x1

def way_to_bahnhof(graph):
    way_to_bahnhof = []
    for ways in graph["ksr"]:
        con1 = ways in graph["ksr"]
        if con1 == True:
            print(con1)
        
way_to_bahnhof(graph)