# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:57:37 2020

@author: TKite
"""

import numpy as np


def get_nth_digit(num, N):
    return int(str(num)[-N])


def get_cell_power(x, y, serial_num):
    power = x + 10
    power *= y
    power += serial_num
    power *= (x + 10)
    power = get_nth_digit(power, 3)
    return power - 5


def coord_score_calc(x, y, size, serial_num):
    score = sum([get_cell_power(a, b, serial_num)
                 for a in [x, x+1, x+2]
                 for b in [y, y+1, y+2]])
    return score


def coord_score_grid(x, y, size, grid):
    score = grid[y:y+size, x:x+size].sum()
    return score


if __name__ == "__main__":
    serial_num = 8772
    grid_length = 299

    grid = [[get_cell_power(x, y, serial_num)
             for x in range(1, grid_length+1)]
            for y in range(1, grid_length+1)]
    grid = np.array(grid, dtype='int64')

    best_coord = max([(x, y, 3)
                      for x in range(1, grid_length+1-3)
                      for y in range(1, grid_length+1-3)],
                     key=lambda c:
                         coord_score_grid(c[0]-1, c[1]-1, c[2], grid))

    print("part 1:")
    print("The best coordinate is {}".format(best_coord))

    best_coord = max([(x, y, s)
                      for s in range(1, grid_length)
                      for x in range(1, grid_length+1-s)
                      for y in range(1, grid_length+1-s)],
                     key=lambda c:
                         coord_score_grid(c[0]-1, c[1]-1, c[2], grid))

    print("part 2:")
    print("This will take a minute...")
    print("The best coordinate is {}".format(best_coord))

    """
    part 1:
    The best coordinate is (235, 31, 3)
    part 2:
    The best coordinate is (241, 65, 10)
    """
