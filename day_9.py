# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:48 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer
from collections import deque

players = 477
last_marble = 70851

class circle_game:
    def __init__(self, last_marble_in, players_in):
        self.circle = deque([0,])
        self.last_marble = last_marble_in
        self.player_scores = [0]*players_in
        self.current_player = 0
        self.current_marble = 0
        self.next_marble = 1

    def show(self):
        zero_loc = self.circle.index(0)
        self.circle.rotate(-zero_loc)
        func = lambda x: "(" + str(x) + ")" if x == self.current_marble \
                         else " " + str(x) + " "
        print(*[func(x) for x in self.circle])
        self.circle.rotate(zero_loc)

    def evolve_game_step(self):
        if (self.next_marble % 23 != 0):
            self.circle.rotate(-2)
            self.circle.append(self.next_marble)
            self.circle.rotate(1)
            self.current_marble = self.next_marble
        else:
            self.circle.rotate(6)
            self.player_scores[self.current_player] += self.next_marble + self.circle.pop()
            self.current_marble = self.circle[0]
        self.next_marble += 1
        self.current_player = (self.current_player + 1) % len(self.player_scores)

    def full_evolve(self):
        while (self.next_marble < self.last_marble):
            self.evolve_game_step()


def part1():
    game = circle_game(70851, 477)
    game.full_evolve()
    print("Top elf score is {}.".format(max(game.player_scores)))

def part2():
    game = circle_game(70851*100, 477)
    game.full_evolve()
    print("Top elf score is {}.".format(max(game.player_scores)))

if __name__ == "__main__":
    timer = Advent_Timer()
    part1()
    timer.checkpoint_hit()
    part2()
    timer.checkpoint_hit()
    timer.end_hit()
