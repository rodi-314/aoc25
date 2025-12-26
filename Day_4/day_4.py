THRESHOLD = 4
DIRECTIONS = (
    (0, 1),
    (1, 0),
    (1, 1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (1, -1),
    (-1, 1),
)


def check(row, col, grid, rows, cols):
    adj_rolls = 0
    for direction in DIRECTIONS:
        adj_row, adj_col = row + direction[0], col + direction[1]
        if adj_row in range(rows) and adj_col in range(cols) and grid[adj_row][adj_col] == '@':
            adj_rolls += 1
        if adj_rolls >= THRESHOLD:
            return False

    return True


def part_1():
    with open('day_4.txt', 'r') as input_file:
        grid = input_file.read().split()
        rows, cols = len(grid), len(grid[0])
        total = 0
        for row in range(rows):
            for col in range(cols):
                total += grid[row][col] == '@' and check(row, col, grid, rows, cols)

        print(f'Part 1: Rolls of paper removed = {total}')


def part_2():
    with open('day_4.txt', 'r') as input_file:
        grid = [[col for col in row] for row in input_file.read().split()]
        rows, cols = len(grid), len(grid[0])
        prev_total = -1
        total = 0
        while total > prev_total:
            prev_total = total
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == '@' and check(row, col, grid, rows, cols):
                        total += 1
                        grid[row][col] = '.'

        print(f'Part 2: Rolls of paper removed = {total}')


def main():
    part_1()
    part_2()


if __name__ == '__main__':
    main()
