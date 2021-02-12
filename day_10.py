# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:57:37 2020

@author: TKite
"""

from aoc_tools import Advent_Timer
import numpy as np


def readfile(filename):
    with open(filename, 'r') as file:
        data = [line.strip() for line in file]
    return data


def process_string(str_in):
    ind1 = str_in.index('<')
    ind2 = str_in.index('>')
    x, y = [int(i) for i in str_in[ind1+1:ind2].split(',')]
    str_in = str_in[ind2+1:]
    ind1 = str_in.index('<')
    ind2 = str_in.index('>')
    vx, vy = [int(i) for i in str_in[ind1+1:ind2].split(',')]
    return np.array([x, y, vx, vy], dtype='int64')


def take_step(all_coords, mult=1):
    all_coords[:, [0, 1]] += mult*all_coords[:, [2, 3]]
    return


def full_evolve(all_coords):
    prev_area = get_grid_area(all_coords)
    seconds = 0
    while True:
        take_step(all_coords)
        area = get_grid_area(all_coords)
        seconds += 1
        if area > prev_area:
            take_step(all_coords, -1)
            return seconds - 1
        prev_area = area

def get_grid_dims(all_coords):
    x_min = min(all_coords[:, 0])
    x_max = max(all_coords[:, 0])
    y_min = min(all_coords[:, 1])
    y_max = max(all_coords[:, 1])
    return [x_min, x_max, y_min, y_max]


def get_grid_area(all_coords):
    dims = get_grid_dims(all_coords)
    return (dims[1] - dims[0])*(dims[3] - dims[2])


def make_grid(all_coords):
    x_min, x_max, y_min, y_max = get_grid_dims(all_coords)
    grid = [['.' for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)]
    for row in all_coords:
        grid[row[1]-y_min][row[0]-x_min] = '#'
    return grid


def show_grid(grid):
    for y in range(len(grid)):
        str_out = ''
        for x in range(len(grid[0])):
            str_out += grid[y][x]
        print(str_out)
    return


def part1(filename):
    data = readfile(filename)
    data = np.array([process_string(line) for line in data])
    full_evolve(data)
    show_grid(make_grid(data))


def part2(filename):
    data = readfile(filename)
    data = np.array([process_string(line) for line in data])
    seconds = full_evolve(data)
    print("This took {} seconds".format(seconds))


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_10.dat")
    timer.checkpoint_hit()
    part2("data/day_10.dat")
    timer.checkpoint_hit()
    timer.end_hit()
