def part_1(s: str) -> int:
    """Solve part 1 for day 6 2022."""
    for i in range(4, len(s) + 1):
        occurences = set(s[i - 4:i])
        if len(occurences) == 4:
            return i
    return -1


def part_2(s: str) -> int:
    """Solve part 2 for day 6 2022."""
    for i in range(14, len(s) + 1):
        occurences = set(s[i - 14:i])
        if len(occurences) == 14:
            return i
    return -1


if __name__ == "__main__":
    print(part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
    print(part_1("bvwbjplbgvbhsrlpgdmjqwftvncz"))
    print(part_1("nppdvjthqldpwncqszvftbrmjlhg"))
    print(part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
    print(part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
