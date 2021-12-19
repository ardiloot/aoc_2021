import numpy as np
from scipy.spatial.transform import Rotation

def read_scanners():
    scanners = []
    with open("input.txt") as fin:    
        while True:
            line = fin.readline()
            if line == "":
                break
            beacons = []
            while True:
                line = fin.readline().strip()
                if line == "":
                    break
                beacons.append(list(map(int, line.split(","))))
            scanners.append(np.array(beacons, dtype=int))
    return scanners

def get_all_rotations():
    rotx = Rotation.from_rotvec(np.pi / 2.0 * np.array([1, 0, 0])).as_matrix().astype(int)
    roty = Rotation.from_rotvec(np.pi / 2.0 * np.array([0, 1, 0])).as_matrix().astype(int)
    rotz = Rotation.from_rotvec(np.pi / 2.0 * np.array([0, 0, 1])).as_matrix().astype(int)
    rotations = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                rotations.append(np.linalg.matrix_power(rotx, i) \
                    .dot(np.linalg.matrix_power(roty, j)) \
                    .dot(np.linalg.matrix_power(rotz, k))
                )
    return np.unique(np.array(rotations), axis=0)

def find_scanner_positions(ref_beacons, target_beacons):
    for i in range(len(ref_beacons)):
        for j in range(len(target_beacons)):
            pos = ref_beacons[i] - target_beacons[j]
            set1 = set(tuple(p) for p in ref_beacons)
            set2 = set(tuple(p) for p in target_beacons + pos)
            if len(set1.intersection(set2)) >= 12:
                return pos


scanners = read_scanners()
rotations = get_all_rotations()
scanner_positions = {0: np.array([0, 0, 0])}
scanner_beacons = {0: scanners[0]}
queue = [0]

while len(queue) > 0:
    ref_scanner_id = queue.pop()
    ref_beacons = scanner_beacons[ref_scanner_id]    
    for i in range(len(scanners)):
        if i in scanner_positions:
            continue
        for rot in rotations:
            target_beacons = np.matmul(rot, scanners[i][:, :, np.newaxis])[:, :, 0]
            pos = find_scanner_positions(ref_beacons, target_beacons)
            if pos is not None:
                scanner_positions[i] = pos
                scanner_beacons[i] = target_beacons + pos
                queue.append(i)
                break

beacons = np.unique([tuple(beacon) for beacons in scanner_beacons.values() for beacon in beacons], axis=0)
print("Task 1:", len(beacons))

res = 0
for p1 in scanner_positions.values():
    for p2 in scanner_positions.values():
        res = max(res, np.abs(p1 - p2).sum())
print("Task 2:", res)
