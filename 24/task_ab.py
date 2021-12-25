
def gen_code():
    code = []
    data_index = 0
    with open("input.txt") as fin:
        for line in fin.readlines():
            tmp = line.strip().split()
            cmd = tmp[0]
            a, b = tmp[1], tmp[2] if len(tmp) > 2 else None

            if cmd == "inp":
                code.append("%s = data[%d];" % (a, data_index))
                data_index += 1
            elif cmd == "add":
                code.append("%s += %s;" % (a, b))
            elif cmd == "mul":
                code.append("%s *= %s;" % (a, b))
            elif cmd == "div":
                code.append("%s /= %s;" % (a, b))
            elif cmd == "mod":
                code.append("%s %%= %s;" % (a, b))
            elif cmd == "eql":
                code.append("%s = int64_t(%s == %s);" % (a, a, b))
            else:
                raise NotImplemetedError()

    for line in code:
        print("    %s" % (line))

gen_code()