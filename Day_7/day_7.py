from copy import deepcopy


def part_1():
    with open('day_7.txt', 'r') as input_file:
        # Simulation
        start_line = input_file.readline().strip()
        beams = set()
        beams.add(start_line.index('S'))
        splits = 0
        input_file.readline()  # Skip redundant line
        for line in input_file:
            for index, char in enumerate(line.strip()):
                if char == '^' and index in beams:
                    beams.add(index - 1)
                    beams.add(index + 1)
                    beams.remove(index)
                    splits += 1
            input_file.readline()

        print(f'Part 1: Number of splits = {splits}')


def part_2():
    with open('day_7.txt', 'r') as input_file:
        # Simulation (1D-DP Pascal's Triangle)
        start_line = input_file.readline().strip()
        prev_line = []
        for char in start_line:
            if char == 'S':
                prev_line.append(1)
            else:
                prev_line.append(0)

        input_file.readline()
        for line in input_file:
            curr_line = deepcopy(prev_line)
            for index, char in enumerate(line.strip()):
                if char == '^' and prev_line[index]:
                    curr_line[index - 1] += prev_line[index]
                    curr_line[index + 1] += prev_line[index]
                    curr_line[index] = 0
            prev_line = curr_line
            input_file.readline()

        print(f'Part 1: Number of splits = {sum(prev_line)}')


def main():
    part_1()
    part_2()


if __name__ == '__main__':
    main()
