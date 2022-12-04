import heapq


def main(part):
    with open("./input.txt", 'r', encoding='UTF-8') as file:
        elves = []
        elf = 0
        calories = 0
        while (line := file.readline()):
            if line.strip() == '':
                heapq.heappush(elves, (-1 * calories, elf))
                elf += 1
                calories = 0
            else:
                calories += int(line)

    if part == 1:
        print(heapq.heappop(elves)[0] * -1)
    else:
        ans = 0
        ans += heapq.heappop(elves)[0] * -1
        ans += heapq.heappop(elves)[0] * -1
        ans += heapq.heappop(elves)[0] * -1
        print(ans)


if __name__ == "__main__":
    main(1)
    main(2)
