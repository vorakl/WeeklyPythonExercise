#!/usr/bin/env python3

from operator import add, sub
import random as rnd
import re

EXERCISE_NUMBER = 10
RAND_RANGE_LEFT = -1
RAND_RANGE_RIGHT = 1
MATH_OPERATIONS = {"+": add, "-": sub}

def generate_exercises(file_name):
    with open(file_name, "w") as f:
        for i in range(1, EXERCISE_NUMBER + 1):
            out = f'[{i:3d}] ' + \
                  f'{rnd.randint(RAND_RANGE_LEFT, RAND_RANGE_RIGHT):3d} ' + \
                  f'{rnd.choice(list(MATH_OPERATIONS))} ' + \
                  f'({rnd.randint(RAND_RANGE_LEFT, RAND_RANGE_RIGHT):3d}) ' + \
                  f'{rnd.choice(list(MATH_OPERATIONS))} ' + \
                  f'({rnd.randint(RAND_RANGE_LEFT, RAND_RANGE_RIGHT):3d}) ' + \
                  f'{rnd.choice(list(MATH_OPERATIONS))} ' + \
                  f'({rnd.randint(RAND_RANGE_LEFT, RAND_RANGE_RIGHT):3d}) ' + \
                  f'= ______' + \
                  '\n'
            f.write(out)

def solve_exercises(file_name):
    exercises = list()

    with open(file_name, "r") as f:
        exercises = f.readlines()

    for exercise in exercises:
        expr = re.findall(r'''\[\s+(\d+)\]          # exercise number
                           \s+(.+?)                 # 1st number
                           \s+([+-])                # operation
                           \s+\(\s*(.+?)\)          # 2nd number
                           \s+([+-])                # operation
                           \s+\(\s*(.+?)\)          # 3rd number
                           \s+([+-])                # operation
                           \s+\(\s*(.+?)\)          # 4th number
                          ''',
                         exercise.strip(),
                         re.X)
        expr = expr[0]

        res = MATH_OPERATIONS[expr[2]](int(expr[1]), int(expr[3]))
        res = MATH_OPERATIONS[expr[4]](res, int(expr[5]))
        res = MATH_OPERATIONS[expr[6]](res, int(expr[7]))

        print(re.sub(r'______', str(res), exercise.strip()))

def main():
    generate_exercises("math_exercises.txt")
    solve_exercises("math_exercises.txt")

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
