# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        data = [int(x) for x in file]
    return data


def part1(filename):
    data = readfile(filename)
    print("Total sum is {}".format(sum(data)))


def part2(filename):
    data = readfile(filename)
    all_freqs = set([0,])

    i = 0
    prev_freq = 0

    while True:
        new_freq = prev_freq + data[i % len(data)]
        if new_freq in all_freqs:
            print("First repeated frequency is {}".format(new_freq))
            break
        all_freqs.add(new_freq)
        prev_freq = new_freq
        i += 1


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_1.dat")
    timer.checkpoint_hit()
    part2("data/day_1.dat")
    timer.checkpoint_hit()
    timer.end_hit()
