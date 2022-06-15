
from tabnanny import check


def pop_and_refresh_candidates(candidates):
    check = candidates.pop(0)
    for ways in graph[check]:
        candidates.append(ways)

graph = {
    "ksr": {"sek": 1},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7},
    "hafenstr": {"bahnhof": 6},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
}

candidates = ["ksr"]
wtBahnhof = []
visited = {}
start = "ksr"

while candidates:
    check = candidates.pop(0)
    visited[check]=start
    for ways in graph[check]:
        if ways in visited:
            pass
        else:
            candidates.append(ways)
        print(candidates)
    start = check
    print(visited)

'''
for p_w_time in way_to_bahnhof:
    way_time = way_time + way_to_bahnhof[p_w_time]
if new_time > way_time:
    way_time = new_time
elif new_time == way_time:
    way_time == way_time, new_time
'''

'''
for places in graph:
    for ways in graph[places]:
        wtBahnhof.append(ways)
        visited[ways]=start        
        start = ways
        if ways in visited:
            pass

        print(wtBahnhof)
        print(visited)
'''
