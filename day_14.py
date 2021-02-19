# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file][0]

def get_digits(num):
    return [int(x) for x in str(num)]

class recipe_game:
    def __init__(self, end_point_in):
        self.recip = [3, 7]
        self.elf_locs = [0, 1]
        self.end_point = end_point_in
        self.end_len = len(get_digits(self.end_point))
        self.history = set()

    def get_string(self, start, end):
        rval = ""
        for x in self.recip[start:end]:
            rval += str(x)
        return rval

    def update_recipes(self, store_history=False):
        current_val = get_digits(sum([self.recip[x] for x in self.elf_locs]))
        self.recip += current_val
        if store_history:
            for i in range(len(current_val)):
                self.history.add(self.get_string(len(self.recip)-i-self.end_len,
                                             len(self.recip)-i))
        self.elf_locs = [(x + 1 + self.recip[x]) % len(self.recip) for x in self.elf_locs]

    def get_sol_p1(self):
        while len(self.recip) < self.end_point+10:
            self.update_recipes()
        return self.get_string(self.end_point, self.end_point+10)

    def get_sol_p2(self):
        while str(self.end_point) not in self.history:
            self.update_recipes(True)
        for i in range(len(self.recip)-self.end_len, -1, -1):
            if self.get_string(i, i + self.end_len) == str(self.end_point):
                return i


def part1(filename):
    end_point = readfile(filename)
    game = recipe_game(readfile(filename))
    print("The next 10 recipes are {}".format(game.get_sol_p1()))


def part2(filename):
    end_point = readfile(filename)
    game = recipe_game(end_point)
    print("Recipe appears after {} steps".format(game.get_sol_p2()))


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_14.dat")
    timer.checkpoint_hit()
    part2("data/day_14.dat")
    timer.checkpoint_hit()
    timer.end_hit()
