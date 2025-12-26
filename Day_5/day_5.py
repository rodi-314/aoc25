def in_range(ingredient, ranges):
    for rng in ranges:
        if ingredient in range(rng[0], rng[1] + 1):
            return True

    return False


def part_1():
    with open('day_5.txt', 'r') as input_file:
        fresh, available = input_file.read().split('\n\n')
        fresh = [list(map(int, rng.split('-'))) for rng in fresh.split()]
        available = list(map(int, available.split()))

        # Merge intervals
        fresh.sort()
        ranges = [fresh[0]]
        for rng in fresh[1:]:
            if rng[0] <= ranges[-1][1] + 1:
                ranges[-1][1] = max(ranges[-1][1], rng[1])
            else:
                ranges.append(rng)

        total = 0
        for ingredient in available:
            total += in_range(ingredient, ranges)

        print(f'Part 1: Number of fresh available ingredients = {total}')
        return ranges


def part_2(ranges):
    print(f'Part 1: Number of fresh ingredients = {sum(rng[1] - rng[0] + 1 for rng in ranges)}')


def main():
    ranges = part_1()
    part_2(ranges)


if __name__ == '__main__':
    main()
