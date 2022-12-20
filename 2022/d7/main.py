from collections import defaultdict
from itertools import accumulate


def d7(filename: str, part: int) -> int:
    with open(filename, 'r', encoding='UTF-8') as f:
        current_dir = []
        directories = defaultdict(int)
        for line in f:
            match line.split():
                case '$', 'cd', '/': current_dir.append('/')
                case '$', 'cd', '..': current_dir.pop()
                case '$', 'cd', x: current_dir.append(x + '/')
                case '$', 'ls': pass
                case 'dir', _: pass
                case f_size, _:
                    for p in accumulate(current_dir):
                        directories[p] += int(f_size)

        if part == 1:
            return sum(v for v in directories.values() if v <= 100000)

        return min(v for v in directories.values() if v >= directories['/'] - 40_000_000)


if __name__ == "__main__":
    print(d7("example.txt", 1))
    print(d7("input.txt", 1))
    print(d7("example.txt", 2))
    print(d7("input.txt", 2))
