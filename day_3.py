# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        data = [x.strip() for x in file]
    return data


class cloth_cut():
    def __init__(self, in_code):
        self.ID, self.x, self.y, self.Lx, self.Ly = read_ID_string(in_code)

    def __str__(self):
        return "ID: {}, x: {}, y: {}, Lx: {}, Ly: {}".format(
            self.ID, self.x, self.y, self.Lx, self.Ly)

    def max_x(self):
        return self.x + self.Lx

    def max_y(self):
        return self.y + self.Ly

    def apply_cut(self, cloth):
        for i in range(self.x, self.max_x()):
            for j in range(self.y, self.max_y()):
                cloth[j][i] += 1
        return cloth

    def independent_cut(self, full_cloth):
        for i in range(self.x, self.max_x()):
            for j in range(self.y, self.max_y()):
                if full_cloth[j][i] != 1:
                    return False
        return True


def read_ID_string(str_in):
    str_in = str_in.split(' ')
    ID = str_in[0][1:]
    x, y = str_in[2].split(',')
    y = y[:-1]
    Lx, Ly = str_in[3].split('x')
    return [int(ID), int(x), int(y), int(Lx), int(Ly)]


def total_size(cloth_cut_list):
    max_x = max([cut.max_x() for cut in cloth_cut_list])
    max_y = max([cut.max_y() for cut in cloth_cut_list])
    return max_x, max_y


def part1(filename):
    input_data = readfile(filename)
    cloth_cut_list = [cloth_cut(x) for x in input_data]
    max_x, max_y = total_size(cloth_cut_list)

    cloth = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for cut in cloth_cut_list:
        cloth = cut.apply_cut(cloth)

    overlaps = sum([sum([1 for x in line if x > 1]) for line in cloth])
    print("The total squares claimed more than once is {}".format(overlaps))


def part2(filename):
    input_data = readfile(filename)
    cloth_cut_list = [cloth_cut(x) for x in input_data]
    max_x, max_y = total_size(cloth_cut_list)

    cloth = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for cut in cloth_cut_list:
        cloth = cut.apply_cut(cloth)

    solution_cut = None

    for cut in cloth_cut_list:
        if cut.independent_cut(cloth):
            solution_cut = cut

    print("The independent cut has ID: {}".format(solution_cut.ID))


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_3.dat")
    timer.checkpoint_hit()
    part2("data/day_3.dat")
    timer.checkpoint_hit()
    timer.end_hit()
