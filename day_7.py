# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        data = [line.strip() for line in file]
    return [(line[5], line[36]) for line in data]


def node_ready(node, current_nodes, rules):
    for rule in rules:
        if node == rule[1] and rule[0] not in current_nodes:
            return False
    return True


def all_nodes_ready(nodes_to_go, current_nodes, rules):
    return set([node for node in nodes_to_go \
                if node_ready(node, current_nodes, rules)])


def sort_all_nodes(rules):
    rval = []
    nodes_to_go = set([x[0] for x in rules]).union([x[1] for x in rules])
    current_nodes = set()
    while len(nodes_to_go):
        next_nodes = list(all_nodes_ready(nodes_to_go, current_nodes, rules))
        next_nodes = sorted(next_nodes)[0]
        rval.append(next_nodes)
        current_nodes.add(next_nodes)
        nodes_to_go.remove(next_nodes)
    return rval


def get_list_string(list_in):
    rval = ""
    for elem in list_in:
        rval += str(elem)
    return rval


def build_full_system(rules, num_workers=5):
    time_taken = -1
    workers = [[None, None] for _ in range(num_workers)]
    nodes_to_go = set([x[0] for x in rules]).union([x[1] for x in rules])
    current_nodes = set()
    nodes_num = len(nodes_to_go)

    while len(current_nodes) != nodes_num:
        for worker in workers:
            if worker[0] is not None:
                worker[1] -= 1
                if worker[1] == 0:
                    current_nodes.add(worker[0])
                    worker[0] = None
                    worker[1] = None
        next_nodes = list(all_nodes_ready(nodes_to_go, current_nodes, rules))
        next_nodes = sorted(next_nodes)
        for worker in workers:
            if worker[0] is None:
                if len(next_nodes):
                    worker[0] = next_nodes.pop(0)
                    worker[1] = ord(worker[0])-4
                    nodes_to_go.remove(worker[0])
        time_taken += 1
    return time_taken


def part1(filename):
    rules = readfile(filename)
    node_list = sort_all_nodes(rules)
    print("Node order is {}.".format(get_list_string(node_list)))


def part2(filename):
    rules = readfile(filename)
    node_list = sort_all_nodes(rules)
    print("Time taken to build is {} seconds.".format(build_full_system(rules)))


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_7.dat")
    timer.checkpoint_hit()
    part2("data/day_7.dat")
    timer.checkpoint_hit()
    timer.end_hit()
