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


def N_letters(my_str, N):
    for char in my_str:
        if my_str.count(char) == N:
            return True
    return False


def letter_diff(str1, str2):
    return sum([str1[i] != str2[i] for i in range(len(str1))])


def remove_diff(str1, str2):
    if letter_diff(str1, str2) != 1:
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return str1[:i] + str1[i+1:]


def part1(filename):
    data = readfile(filename)
    two_num = sum([N_letters(x, 2) for x in data])
    three_num = sum([N_letters(x, 3) for x in data])
    print("The checksum is {}".format(two_num*three_num))


def part2(filename):
    data = readfile(filename)
    for i, a in enumerate(data):
        for j, b in enumerate(data[i+1:]):
            rval = remove_diff(a, b)
            if rval:
                print("The answer is\n{}".format(rval))
                return


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_2.dat")
    timer.checkpoint_hit()
    part2("data/day_2.dat")
    timer.checkpoint_hit()
    timer.end_hit()
