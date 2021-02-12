# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:32:29 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer


def valid_reac(a, b):
    if a == a.lower():
        if b == a.upper():
            return True
    else:
        if b == a.lower():
            return True
    return False


class polymer():
    def __init__(self, code_in):
        self.code = code_in

    def full_react(self):
        i = len(self.code)-2
        self.simplified = True
        while i >= 0:
            if valid_reac(self.code[i], self.code[i+1]):
                self.code = self.code[:i] + self.code[i+2:]
            i -= 1
        return

    def get_length(self):
        return len(self.code)

    def get_unit_types(self):
        rval = set()
        for unit in self.code:
            rval.add(unit.lower())
        return rval

    def remove_unit(self, unit):
        i = 0
        while i < len(self.code):
            if self.code[i].lower() == unit:
                self.code = self.code[:i] + self.code[i+1:]
                continue
            i += 1


def part1(filename):
    data = open(filename, 'r').readline()
    my_pol = polymer(data)
    my_pol.full_react()
    print("The length after reacting is {}".format(my_pol.get_length()))

def part2(filename):
    data = open(filename, 'r').readline()
    my_pol = polymer(data)
    my_pol.full_react()

    unit_length_dict = {}

    for unit in my_pol.get_unit_types():
        unit_length_dict[unit] = polymer(my_pol.code)
        unit_length_dict[unit].remove_unit(unit)
        unit_length_dict[unit].full_react()

    max_unit = min(unit_length_dict.keys(),
                   key=lambda x: unit_length_dict[x].get_length())
    print("The shortest length is found by removing {}/{}, with length {}"
          .format(max_unit,
                  max_unit.upper(),
                  unit_length_dict[max_unit].get_length()))

if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_5.dat")
    timer.checkpoint_hit()
    part2("data/day_5.dat")
    timer.checkpoint_hit()
    timer.end_hit()
