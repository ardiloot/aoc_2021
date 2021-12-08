import itertools

correct_digits = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

def fits(digits, mapping):
    new_digits = []
    for digit in digits:
        new_digit = "".join(sorted(mapping[d] for d in digit))
        if new_digit not in correct_digits or new_digit in new_digits:
            return False
        new_digits.append(new_digit)
    return True

with open("input.txt") as fin:
    lines = fin.readlines()

res = 0
for line in lines:
    a, b = line.strip().split(" | ")
    digits = a.split()

    mapping = None
    for perm in itertools.permutations("abcdegf"):
        mapping = dict(zip("abcdegf", perm))
        if fits(digits, mapping):
            break

    value = 0
    for output in b.split():
        value *= 10
        value += correct_digits.index("".join(sorted(mapping[d] for d in output)))
    res += value
print(res)