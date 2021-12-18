
def split_pair(line):
    split_pos = -1
    opened = 0
    for i, c in enumerate(line):
        if c == "[":
            opened += 1
        elif c == "]":
            opened -= 1
        if opened == 1 and c == ",":
            split_pos = i
            break
    if split_pos >= 0:
        return line[1:split_pos], line[split_pos+1:-1]
    else:
        return (line,)


class Number:

    def __init__(self, line, parent=None):
        self._parent = parent
        self._children = []
        self._value = None

        pair = split_pair(line)
        if len(pair) < 2:
            self._value = int(pair[0])
        else:
            self._children = [Number(p, self) for p in pair]

    def set_zero(self):
        self._children = []
        self._value = 0

    def add(self, n):
        res = Number("0")
        res._value = None
        res._children = [self, n]
        self._parent = n._parent = res
        return res

    def reduce(self):
        while True:
            if self._explode():
                continue
            if self._split():
                continue
            break

    def magnitude(self):
        if self._value is not None:
            return self._value
        return 3 * self._children[0].magnitude() + 2 * self._children[1].magnitude()

    def to_line(self):
        if self._value is not None:
            return str(self._value)
        else:
            return "[%s,%s]" % (self._children[0].to_line(), self._children[1].to_line())
    
    def _explode(self):
        n_explode = self._find_pair_to_explode()
        if n_explode is None:
            return False

        n_left = n_explode._find_number_to_left()
        if n_left is not None:
            n_left._value += n_explode._children[0]._value

        n_right = n_explode._find_number_to_right()
        if n_right is not None:
            n_right._value += n_explode._children[1]._value
        n_explode.set_zero()
        return True

    def _split(self):
        n_split = self._find_to_split()
        if n_split is None:
            return None
        a = n_split._value // 2
        b = n_split._value - a
        n_split._value = None
        n_split._children = [Number(str(a), n_split), Number(str(b), n_split)]
        return True

    def _find_pair_to_explode(self, level=0):
        if level == 4 and self._value is None:
            return self
        for n in self._children:
            res = n._find_pair_to_explode(level + 1)
            if res is not None:
                return res

    def _find_to_split(self):
        if self._value is not None and self._value >= 10:
            return self
        for n in self._children:
            res = n._find_to_split()
            if res is not None:
                return res 

    def _find_number_to_left(self):
        return self._find_number_to_side(0)
       
    def _find_number_to_right(self):
        return self._find_number_to_side(1)

    def _find_number_to_side(self, index):
        cur_node = self
        while cur_node._parent is not None and cur_node._parent._children[index] == cur_node:
            cur_node = cur_node._parent
        split_node = cur_node._parent
        if split_node is None:
            return None
        node = split_node._children[index]
        while node._value is None:
            node = node._children[index ^ 1]
        return node
        

with open("input.txt") as fin:
    lines = [line.strip() for line in fin.readlines()]

# Task 1
n = Number(lines[0])
for line in lines[1:]:
    n = n.add(Number(line))
    n.reduce()
print("Task1:", n.magnitude())
    
# Task 2
max_mag = 0
for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines):
        if i == j:
            continue
        n = Number(line1).add(Number(line2))
        n.reduce()
        max_mag = max(max_mag, n.magnitude())
print("Task2:", max_mag)
