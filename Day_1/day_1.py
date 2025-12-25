STARTING_POSITION = 50
DIAL_SIZE = 100
COUNT_POSITION = 0


def main():
    with open('day_1_test.txt', 'r') as input_file:
        position = STARTING_POSITION
        times = 0
        for line in input_file.readlines():
            line = line.strip()
            direction, turns = line[0], int(line[1:])
            if direction == 'L':
                position = (position - turns) % DIAL_SIZE
            else:
                position = (position + turns) % DIAL_SIZE
            times += position == COUNT_POSITION

        print(f'Part 1: Number of times dial points at {COUNT_POSITION} = {times}')

    with open('day_1.txt', 'r') as input_file:
        position = STARTING_POSITION
        times = 0
        for line in input_file.readlines():
            line = line.strip()
            direction, turns = line[0], int(line[1:])
            if direction == 'L':
                if position == 0:
                    times += turns // DIAL_SIZE
                elif turns >= position:
                    times += 1 + (turns - position) // DIAL_SIZE
                position = (position - turns) % DIAL_SIZE
            else:
                if position == 0:
                    times += turns // DIAL_SIZE
                elif turns >= DIAL_SIZE - position:
                    times += 1 + (turns - (DIAL_SIZE - position)) // DIAL_SIZE
                position = (position + turns) % DIAL_SIZE

        print(f'Part 2: Number of times dial points at {COUNT_POSITION} = {times}')


if __name__ == '__main__':
    main()
