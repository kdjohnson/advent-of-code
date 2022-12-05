def part1(crates, filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        _, instructions = file.read().split("\n\n")
        instructions = instructions.split('\n')
        for instruction in instructions:
            if len(instruction) == 18:
                iter = int(instruction[5:7])
                start = int(instruction[12:13]) - 1
                stop = int(instruction[17:18]) - 1
            else:
                iter = int(instruction[5:8])
                start = int(instruction[13:14]) - 1
                stop = int(instruction[18:19]) - 1

            for _ in range(iter):
                if len(crates[start]) > 0:
                    crates[stop].append(crates[start].pop())

        ans = []
        for c in crates:
            ans.append(c.pop())

        return ''.join(ans)


def part2(crates, filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        _, instructions = file.read().split("\n\n")
        instructions = instructions.split('\n')
        for instruction in instructions:
            if len(instruction) == 18:
                iter = int(instruction[5:7])
                start = int(instruction[12:13]) - 1
                stop = int(instruction[17:18]) - 1
            else:
                iter = int(instruction[5:8])
                start = int(instruction[13:14]) - 1
                stop = int(instruction[18:19]) - 1

            if len(crates[start]) > 0:
                crates[stop].extend(crates[start][-iter:])
                del crates[start][-iter:]

        ans = []
        for c in crates:
            if len(c) > 0:
                ans.append(c.pop())

        return ''.join(ans)


if __name__ == "__main__":
    print(part1([
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ], "example.txt"))
    print(part1([
        ["Z", "P", "M", "H", "R"],
        ["P", "C", "J", "B"],
        ["S", "N", "H", "G", "L", "C", "D"],
        ["F", "T", "M", "D", "Q", "S", "R", "L"],
        ["F", "S", "P", "Q", "B", "T", "Z", "M"],
        ["T", "F", "S", "Z", "B", "G"],
        ["N", "R", "V"],
        ["P", "G", "L", "T", "D", "V", "C", "M"],
        ["W", "Q", "N", "J", "F", "M", "L"]
    ], "input.txt"))
    print(part2([
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ], "example.txt"))
    print(part2([
        ["Z", "P", "M", "H", "R"],
        ["P", "C", "J", "B"],
        ["S", "N", "H", "G", "L", "C", "D"],
        ["F", "T", "M", "D", "Q", "S", "R", "L"],
        ["F", "S", "P", "Q", "B", "T", "Z", "M"],
        ["T", "F", "S", "Z", "B", "G"],
        ["N", "R", "V"],
        ["P", "G", "L", "T", "D", "V", "C", "M"],
        ["W", "Q", "N", "J", "F", "M", "L"]
    ], "input.txt"))
