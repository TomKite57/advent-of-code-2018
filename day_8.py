# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:48 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer

def readfile(filename):
    # Get raw data from file
    with open(filename) as file:
        line = [line.strip() for line in file][0]

    # interpret each line as two CSV ints
    data = [int(x) for x in line.split(' ')]
    return data


class node:
    def __init__(self, code, pos=0):
        self.num_child = code[pos]
        self.num_meta = code[pos+1]
        self.children = []
        pos += 2
        for _ in range(self.num_child):
            self.children.append(node(code, pos))
            pos = self.children[-1].next_pos
        self.metadata = []
        for _ in range(self.num_meta):
            self.metadata.append(code[pos])
            pos += 1
        self.next_pos = pos

    def total_tree_meta_p1(self):
        meta = sum(self.metadata)
        for child in self.children:
            meta += child.total_tree_meta_p1()
        return meta

    def total_tree_meta_p2(self):
        if self.num_child == 0:
            return sum(self.metadata)
        total_meta = 0
        for meta in self.metadata:
            if (0 <= meta <= self.num_child):
                total_meta += self.children[meta-1].total_tree_meta_p2()
        return total_meta


def part1(filename):
    data = readfile(filename)
    tree = node(data)
    total_count = tree.total_tree_meta_p1()

    print("The total sum of metadata is {}.".format(total_count))


def part2(filename):
    data = readfile(filename)
    tree = node(data)
    total_count = tree.total_tree_meta_p2()

    print("The total sum of metadata is {}.".format(total_count))


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_8.dat")
    timer.checkpoint_hit()
    part2("data/day_8.dat")
    timer.checkpoint_hit()
    timer.end_hit()
