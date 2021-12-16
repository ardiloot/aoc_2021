import numpy as np

def parse(p):
    version = int(data[p:p+3], 2)
    p += 3
    type_id = int(data[p:p+3], 2)
    p += 3

    if type_id == 4:
        payload = []
        while True:
            is_last = data[p] == "0"
            payload.append(data[p+1:p+5])
            p += 5
            if is_last:
                break
        value = int("".join(payload), 2)
        return p, value

    else:
        length_type = data[p]
        p += 1        
        values = []
        if length_type == "0":
            length = int(data[p:p+15], 2)
            p += 15
            read_until = p + length
            while p != read_until:
                p, value = parse(p)
                values.append(value)
        else:
            num_packets = int(data[p:p+11], 2)
            p += 11
            for i in range(num_packets):
                p, value = parse(p)
                values.append(value)
        res = 0
        if type_id == 0:
            res = sum(values)
        elif type_id == 1:
            res = np.prod(np.array(values, dtype=np.int64))
        elif type_id == 2:
            res = min(values)
        elif type_id == 3:
            res = max(values)
        elif type_id == 5:
            res = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            res = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            res = 1 if values[0] == values[1] else 0
        return p, res

with open("input.txt") as fin:
    line = fin.readline().strip()
    data = "".join("{0:04b}".format(int(a, 16)) for a in line)
    
print(parse(0))