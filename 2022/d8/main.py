def is_lower(t_line: set, cell: int) -> bool:
    return all(t < cell for t in t_line)


def is_visible(field: list[list[int]], i: int, j: int, i_range: int, j_range: int, cell: int) -> bool:
    top = set()
    for t in range(0, i):
        top.add(field[t][j])

    right = set()
    for t in range(j + 1, j_range):
        right.add(field[i][t])

    bottom = set()
    for t in range(i + 1, i_range):
        bottom.add(field[t][j])

    left = set()
    for t in range(0, j):
        left.add(field[i][t])

    return is_lower(top, cell) or is_lower(right, cell) or is_lower(bottom, cell) or is_lower(left, cell)


def tree_line(field: list[list[int]], i: int, j: int, i_range: int, j_range: int, cell: int) -> int:
    top_tree_line = []
    for t in range(i - 1, -1, -1):
        if field[t][j] >= cell:
            top_tree_line.append(field[t][j])
            break

        if field[t][j] < cell:
            top_tree_line.append(field[t][j])

    right_tree_line = []
    for t in range(j + 1, j_range):
        if field[i][t] >= cell:
            right_tree_line.append(field[i][t])
            break

        if field[i][t] < cell:
            right_tree_line.append(field[i][t])

    bottom_tree_line = []
    for t in range(i + 1, i_range):
        if field[t][j] >= cell:
            bottom_tree_line.append(field[t][j])
            break

        if field[t][j] < cell:
            bottom_tree_line.append(field[t][j])

    left_tree_line = []
    for t in range(j - 1, -1, -1):
        if field[i][t] >= cell:
            left_tree_line.append(field[i][t])
            break

        if field[i][t] < cell:
            left_tree_line.append(field[i][t])

    return len(top_tree_line) * len(right_tree_line) * len(bottom_tree_line) * len(left_tree_line)


def treehouse(filename: str, part: int) -> int:
    with open(filename, 'r', encoding='UTF-8') as f:
        trees = [line.split() for line in f]
        field = []
        for t in trees:
            for c in t:
                row = [*map(int, str(c))]
                field.append(row)

        visible_trees, score = 0, 0
        for i, row in enumerate(field):
            for j, cell in enumerate(row):
                if i - 1 < 0:
                    visible_trees += 1
                elif j - 1 < 0:
                    visible_trees += 1
                elif i + 1 == len(field):
                    visible_trees += 1
                elif j + 1 == len(row):
                    visible_trees += 1
                else:
                    if part == 1 and is_visible(field, i, j, len(field), len(row), cell):
                        visible_trees += 1
                    else:
                        score = max(score,
                                    tree_line(field, i, j, len(field), len(row), cell))
    if part == 1:
        return visible_trees

    return score


if __name__ == "__main__":
    print(treehouse('example.txt', 1))
    print(treehouse('input.txt', 1))
    print(treehouse('example.txt', 2))
    print(treehouse('input.txt', 2))
