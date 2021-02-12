# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:48 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer
from collections import deque


def readfile(filename):
    with open(filename, 'r') as file:
        line = file.readline().split(' ')
    return int(line[0]), int(line[-2])


class circle_game:
    def __init__(self, players_in, last_marble_in):
        self.circle = deque([0,])
        self.last_marble = last_marble_in
        self.player_scores = [0]*players_in
        self.next_marble = 1

    def evolve_game_step(self):
        if (self.next_marble % 23 != 0):
            self.circle.rotate(-2)
            self.circle.append(self.next_marble)
            self.circle.rotate(1)
        else:
            self.circle.rotate(6)
            self.player_scores[self.next_marble % len(self.player_scores)] += self.next_marble + self.circle.pop()
        self.next_marble += 1

    def full_evolve(self):
        while (self.next_marble < self.last_marble):
            self.evolve_game_step()


def part1(filename):
    players, last_marble = readfile(filename)
    game = circle_game(players, last_marble)
    game.full_evolve()
    print("Top elf score is {}.".format(max(game.player_scores)))

def part2(filename):
    players, last_marble = readfile(filename)
    game = circle_game(players, last_marble*100)
    game.full_evolve()
    print("Top elf score is {}.".format(max(game.player_scores)))

if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_9.dat")
    timer.checkpoint_hit()
    part2("data/day_9.dat")
    timer.checkpoint_hit()
    timer.end_hit()
