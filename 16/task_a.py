
def parse(p):
    global sum_versions
    version = int(data[p:p+3], 2)
    sum_versions += version
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
    else:
        length_type = data[p]
        p += 1
        
        if length_type == "0":
            length = int(data[p:p+15], 2)
            p += 15
            read_until = p + length
            while p < read_until:
                p = parse(p)
        else:
            num_packets = int(data[p:p+11], 2)
            p += 11
            for i in range(num_packets):
                p = parse(p)
    return p

with open("input.txt") as fin:
    line = fin.readline().strip()
    data = "".join("{0:04b}".format(int(a, 16)) for a in line)

sum_versions = 0
parse(0)
print(sum_versions)