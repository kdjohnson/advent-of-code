def main(filename, part):
    with open(filename, 'r', encoding='UTF-8') as file:
        lines = [line.strip() for line in file]
        counter = 0
        for line in lines:
            p1, p2 = line.split(',')[0], line.split(',')[1]
            r1, r2 = {*range(int(p1.split('-')[0]), int(p1.split('-')[1]) + 1)}, {*range(
                int(p2.split('-')[0]), int(p2.split('-')[1]) + 1)}
            if part == 1:
                if r1.issubset(r2) or r2.issubset(r1):
                    counter += 1
            else:
                if len(r1.intersection(r2)) != 0:
                    counter += 1
        return counter


if __name__ == "__main__":
    print(main("example.txt", 1))
    print(main("input.txt", 1))
    print(main("example.txt", 2))
    print(main("input.txt", 2))
