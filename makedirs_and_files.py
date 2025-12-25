import os

PARENT_DIRECTORY = r'C:\Users\rodi3\Documents\aoc25'

for i in range(1, 13):
    directory = os.path.join(PARENT_DIRECTORY, f'Day_{i}')
    os.makedirs(directory, exist_ok=True)

    with open('template.py', 'r') as template, \
            open(os.path.join(directory, f'day_{i}.py'), 'w') as script, \
            open(os.path.join(directory, f'day_{i}.txt'), 'w'), \
            open(os.path.join(directory, f'day_{i}_test.txt'), 'w'):
        script.write(template.read().replace('day_x_test.txt', f'day_{i}_test.txt'))
