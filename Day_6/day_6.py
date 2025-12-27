def part_1():
    with open('day_6.txt', 'r') as input_file:
        grid = [line.split() for line in input_file.read().split('\n')]
        total = 0
        for col in range(len(grid[0])):
            if grid[-1][col] == '+':
                curr_total = 0
                for row in grid[:-1]:
                    curr_total += int(row[col])
            else:
                curr_total = 1
                for row in grid[:-1]:
                    curr_total *= int(row[col])

            total += curr_total

        print(f'Part 1: Grand total = {total}')


def get_max_row_len(grid):
    max_row_len = 0
    for row in grid:
        max_row_len = max(max_row_len, len(row))

    return max_row_len


def part_2():
    with open('day_6.txt', 'r') as input_file:
        grid = input_file.read().split('\n')
        total = 0
        for col in range(get_max_row_len(grid)):
            # Check operation
            if col < len(grid[-1]) and grid[-1][col] == '+':
                curr_total = 0
                is_add = True
            elif col < len(grid[-1]) and grid[-1][col] == '*':
                curr_total = 1
                is_add = False

            # Form number
            number = ''
            for row in grid[:-1]:
                if col < len(row) and row[col] != ' ':
                    number += row[col]

            # Perform operation
            if number:
                if is_add:
                    curr_total += int(number)
                else:
                    curr_total *= int(number)
            else:
                total += curr_total

        total += curr_total

        print(f'Part 2: Grand total = {total}')


def main():
    part_1()
    part_2()


if __name__ == '__main__':
    main()
