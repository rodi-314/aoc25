import os

PARENT_DIRECTORY = r'C:\Users\rodi3\Documents\aoc25'

for i in range(12, 13):
    directory = os.path.join(PARENT_DIRECTORY, f'Day_{i}')
    os.makedirs(directory, exist_ok=True)

    with open('template.py', 'r') as template, \
            open(os.path.join(directory, f'day_{i}.py'), 'a') as script, \
            open(os.path.join(directory, f'day_{i}.txt'), 'a'), \
            open(os.path.join(directory, f'day_{i}_test.txt'), 'a'):
        script.write(template.read())
