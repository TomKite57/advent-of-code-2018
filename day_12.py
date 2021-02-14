# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:57:37 2020

@author: TKite
"""

from aoc_tools import Advent_Timer

def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    initial_condition = lines[0].strip('initial state: ')
    rules = [line.split(' => ') for line in lines[2:]]
    rule_dict = {}
    for r in rules:
        rule_dict[r[0]] = r[1]
    return initial_condition, rule_dict

class planter:
    def __init__(self, init_cond_in, rules_in):
        self.plants = init_cond_in
        self.rules = rules_in
        self.index_start = 0
        self.iteration = 0
        self.adapt_planter()
        self.history = {self.plants: [self.iteration, self.index_start]}
        self.repeated = False

    def adapt_planter(self):
        # Expand on left
        while '#' in self.plants[:3]:
            self.plants = '.' + self.plants
            self.index_start -= 1
        # Contract on left
        while '#' not in self.plants[:4]:
            self.plants = self.plants[1:]
            self.index_start += 1
        # Expand on right
        while '#' in self.plants[-3:]:
            self.plants = self.plants + '.'
        # Contract on right
        while '#' not in self.plants[-4:]:
            self.plants = self.plants[:-1]

    def force_manual_evol(self):
        new_plants = '..'
        for i in range(2, len(self.plants)-2):
            new_plants += self.rules[self.plants[i-2:i+3]]
        new_plants += '..'
        self.plants = new_plants
        self.adapt_planter()
        self.iteration += 1

    def check_repeat(self):
        if self.plants in self.history:
            self.repeated = True
        else:
            self.history[self.plants] =  [self.iteration, self.index_start]

    def evolve_to_step_N(self, N):
        while self.iteration < N:
            if not self.repeated:
                self.force_manual_evol()
                self.check_repeat()
            else:
                prev_it, prev_ind = self.history[self.plants]
                delta_it = self.iteration - prev_it
                prev_ind = self.index_start - prev_ind
                loop_num = (N - self.iteration) // delta_it
                self.iteration += loop_num*delta_it
                self.index_start += loop_num*prev_ind
                for _ in range(N-self.iteration):
                    self.force_manual_evol()

    def outcount(self):
        return sum([self.index_start + i for i,char in enumerate(self.plants) if char == '#'])


def part1(filename):
    initial_cond, rule_dict = readfile(filename)
    my_planter = planter(initial_cond, rule_dict)
    my_planter.evolve_to_step_N(20)
    print("After {} steps the pot count is {}.".format(20, my_planter.outcount()))


def part2(filename):
    initial_cond, rule_dict = readfile(filename)
    my_planter = planter(initial_cond, rule_dict)
    my_planter.evolve_to_step_N(50000000000)
    print("After {} steps the pot count is {}.".format(50000000000, my_planter.outcount()))

if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_12.dat")
    timer.checkpoint_hit()
    part2("data/day_12.dat")
    timer.checkpoint_hit()
    timer.end_hit()
