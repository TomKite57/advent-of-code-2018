# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:57:37 2020

@author: TKite
"""

from aoc_tools import Advent_Timer
import numpy as np

GRID_LENGTH = 300

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


def part1(filename):
    serial_num = int(open(filename, 'r').readline().strip())

    grid = [[get_cell_power(x, y, serial_num)
             for x in range(1, GRID_LENGTH)]
            for y in range(1, GRID_LENGTH)]
    grid = np.array(grid, dtype='int')

    best_coord = max([(x, y, 3)
                      for x in range(1, GRID_LENGTH-3)
                      for y in range(1, GRID_LENGTH-3)],
                     key=lambda c:
                         coord_score_grid(c[0]-1, c[1]-1, c[2], grid))

    print("The best coordinate is {}".format(best_coord))


def part2(filename):
    serial_num = int(open(filename, 'r').readline().strip())

    grid = [[get_cell_power(x, y, serial_num)
             for x in range(1, GRID_LENGTH)]
            for y in range(1, GRID_LENGTH)]
    grid = np.array(grid, dtype='int')

    best_coord = max([(x, y, s)
                      for s in range(1, GRID_LENGTH-1)
                      for x in range(1, GRID_LENGTH-s)
                      for y in range(1, GRID_LENGTH-s)],
                     key=lambda c:
                         coord_score_grid(c[0]-1, c[1]-1, c[2], grid))

    print("The best coordinate is {}".format(best_coord))

if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_11.dat")
    timer.checkpoint_hit()
    part2("data/day_11.dat")
    timer.checkpoint_hit()
    timer.end_hit()

    """
    part 1:
    The best coordinate is (235, 31, 3)
    part 2:
    The best coordinate is (241, 65, 10)
    """
