def main(filename, part):
    with open(filename, 'r', encoding='UTF-8') as file:
        score = 0
        while (line := file.readline()):
            rnd = line.strip().split(" ")
            opp, player = rnd[0], rnd[1]
            if part == 1:
                score += rules_pt1(player, opp)
            else:
                score += rules_pt2(player, opp)
        return score


def rules_pt1(p1, p2):
    match p1:
        case "X":
            match p2:
                case "A":
                    return 4
                case "B":
                    return 1
                case "C":
                    return 7
        case "Y":
            match p2:
                case "A":
                    return 8
                case "B":
                    return 5
                case "C":
                    return 2
        case "Z":
            match p2:
                case "A":
                    return 3
                case "B":
                    return 9
                case "C":
                    return 6


def rules_pt2(p1, p2):
    match p1:
        case "X":
            match p2:
                case "A":
                    return 3
                case "B":
                    return 1
                case "C":
                    return 2
        case "Y":
            match p2:
                case "A":
                    return 4
                case "B":
                    return 5
                case "C":
                    return 6
        case "Z":
            match p2:
                case "A":
                    return 8
                case "B":
                    return 9
                case "C":
                    return 7


if __name__ == "__main__":
    print(main("example.txt", 1))
    print(main("input.txt", 1))

    print(main("example.txt", 2))
    print(main("input.txt", 2))
