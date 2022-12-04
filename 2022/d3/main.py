P = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}


def main(filename, part):

    with open(filename, 'r', encoding='UTF-8') as file:
        lines = [line.strip() for line in file]
        priorities = []
        if part == 1:
            for sack in lines:
                priorities.append(get_priority_pt1(sack))
        else:
            groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]

            for g in groups:
                s1 = get_priority_pt_2(g[0])
                s2 = get_priority_pt_2(g[1])
                s3 = get_priority_pt_2(g[2])
                s = s1 & s2 & s3
                priorities.append(s.pop())

        return sum(priorities)


def get_priority_pt1(line):
    l = len(line)
    c1 = line[:(l//2)]
    c2 = line[l//2:]
    s2 = {P[c] for c in c2}
    s1 = {P[c] for c in c1}
    return s1.intersection(s2).pop()


def get_priority_pt_2(line):
    return {P[c] for c in line}


if __name__ == "__main__":
    print(main("example.txt", 1))
    print(main("input.txt", 1))
    print(main("example.txt", 2))
    print(main("input.txt", 2))
