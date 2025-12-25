NO_OF_BATTERIES = 12


def main():
    with open('day_3.txt', 'r') as input_file:
        total_joltage = 0
        for line in input_file:
            bank = line.strip()
            left = bank[0]
            max_joltage = '0'

            # 2 pointers, one pass
            for right in bank[1:]:
                max_joltage = max(max_joltage, left + right)
                if right > left:
                    left = right
            total_joltage += int(max_joltage)

        print(f'Part 1: Total output joltage = {total_joltage}')

    with open('day_3.txt', 'r') as input_file:
        total_joltage = 0
        for line in input_file:
            bank = line.strip()
            bank_len = len(bank)

            # 2 pointers for each battery
            prev_index = -1
            max_joltage = ''
            for digit in range(NO_OF_BATTERIES):
                curr_index = prev_index + 1
                for index in range(prev_index + 2, bank_len - (NO_OF_BATTERIES - 1 - digit)):
                    if bank[index] > bank[curr_index]:
                        curr_index = index

                prev_index = curr_index
                max_joltage += bank[curr_index]

            total_joltage += int(max_joltage)

        print(f'Part 2: Total output joltage = {total_joltage}')


if __name__ == '__main__':
    main()
