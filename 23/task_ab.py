import numpy as np

cache = {}
ap_cost = {"A": 1, "B": 10, "C": 100, "D": 1000}
room_pos = [2, 4, 6, 8]
hallway_positions = [0, 1, 3, 5, 7, 9, 10]
room_targets = ["A", "B", "C", "D"]

def is_room_finished(room_nr):
    for ap in rooms[room_nr]:
        if ap != room_targets[room_nr]:
            return False
    return True

def is_all_rooms_fully_finished():
    for i, room in enumerate(rooms):
        if len(room) != N or not is_room_finished(i):
            return False
    return True

def is_hallway_free(room_nr, hwp, ends=False):
    a, b = room_pos[room_nr], hwp
    for j in range(min(a, b), max(a, b) + 1):
        if not ends and (j == a or j == b):
            continue
        if hallway[j] != "":
            return False
    return True

def move_to_room(room_nr, hwp):
    ap = hallway[hwp]
    rooms[room_nr].append(ap)
    hallway[hwp] = ""
    return ap_cost[ap] * (abs(hwp - room_pos[room_nr]) + (N + 1 - len(rooms[room_nr])))

def move_to_hallway(room_nr, hwp):
    ap = rooms[room_nr].pop()
    hallway[hwp] = ap
    return ap_cost[ap] * (abs(hwp - room_pos[room_nr]) + (N - len(rooms[room_nr])))

def solve():
    cache_index = (tuple(hallway), tuple(tuple(room) for room in rooms))
    if cache_index in cache:
        return cache[cache_index]
    if is_all_rooms_fully_finished():
        return 0

    res = 1000000
    for room_nr, room in enumerate(rooms):
        room_finished = is_room_finished(room_nr)
        if room_finished and len(room) >= N:
            # Room is fully occupied by correct amphipods
            continue
        elif room_finished:
            # Move amphipod from hallway to final room
            for hwp in hallway_positions:
                if hallway[hwp] != room_targets[room_nr] or not is_hallway_free(room_nr, hwp):
                    continue
                cost = move_to_room(room_nr, hwp)
                res = min(res, solve() + cost)
                move_to_hallway(room_nr, hwp)
        else:
            # Move to hallway
            for hwp in hallway_positions:
                if not is_hallway_free(room_nr, hwp, ends=True):
                    continue
                cost = move_to_hallway(room_nr, hwp)
                res = min(res, solve() + cost)
                move_to_room(room_nr, hwp)
       
    cache[cache_index] = res
    return res

rooms = [
    ["B", "D", "D", "D"],
    ["C", "B", "C", "A"],
    ["B", "A", "B", "C"],
    ["A", "C", "A", "D"],
]
hallway = ["" for _ in range(11)]
N = len(rooms[0])

res = solve()
print("result:", res)