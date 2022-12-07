from collections import Counter


def part_1(s: str) -> int:
    """Solve part 1 for day 6 2022."""
    for i in range(len(s)):
        for j in range(i + 4, len(s)):
            occurences = Counter(s[i:j])
            if not any(count >= 2 for count in occurences.values()):
                return j
            break

    return -1


def part_2(s: str) -> int:
    """Solve part 2 for day 6 2022."""
    for i in range(len(s)):
        for j in range(i + 14, len(s)):
            occurences = Counter(s[i:j])
            if not any(count >= 2 for count in occurences.values()):
                return j
            break

    return -1


if __name__ == "__main__":
    print(part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
    print(part_1("bvwbjplbgvbhsrlpgdmjqwftvncz"))
    print(part_1("nppdvjthqldpwncqszvftbrmjlhg"))
    print(part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
    print(part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))
