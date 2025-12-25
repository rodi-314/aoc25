def check_each_repetition(num, divisor):
    prev = num % divisor
    num //= divisor
    while num:
        curr = num % divisor
        if prev != curr:
            return False
        prev = curr
        num //= divisor

    return True


def check_repetitions(num):
    divisor = 10
    num_str = str(num)
    for i in range(len(num_str) // 2):
        if len(num_str) % (i + 1) == 0 and check_each_repetition(num, divisor):
            return True
        divisor *= 10

    return False


def main():
    with open('day_2.txt', 'r') as input_file:
        total = 0
        for rng in input_file.read().split(','):
            start, end = rng.split('-')
            start, end = int(start), int(end)
            for num in range(start, end + 1):
                num_str = str(num)
                if len(num_str) % 2 == 0 and num_str[:len(num_str) // 2] == num_str[len(num_str) // 2:]:
                    total += num

        print(f'Part 1: Sum of invalid IDs = {total}')

    with open('day_2.txt', 'r') as input_file:
        total = 0
        for rng in input_file.read().split(','):
            start, end = rng.split('-')
            start, end = int(start), int(end)
            for num in range(start, end + 1):
                if check_repetitions(num):
                    total += num

        print(f'Part 2: Sum of invalid IDs = {total}')


if __name__ == '__main__':
    main()
