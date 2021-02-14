# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer

direction_dict = {'>': [1, 0],
                  '^': [0, -1],
                  '<': [-1, 0],
                  'v': [0, 1]}

def readfile(filename):
    with open(filename, 'r') as file:
        data = [line.strip('\n') for line in file]
    map = []
    carts_data = []
    for y, line in enumerate(data):
        map_line = []
        for x, char in enumerate(line):
            if char in ['<', '>']:
                map_line.append('-')
                carts_data.append([x, y, char])
            elif char in ['^', 'v']:
                map_line.append('|')
                carts_data.append([x, y, char])
            else:
                map_line.append(char)
        map.append(map_line)
    return map, [cart(*x, map) for x in carts_data]


def turn_corner(direc, track):
    if direc == '>':
        if track == '/':
            return '^'
        else:
            return 'v'
    if direc == '<':
        if track == '/':
            return 'v'
        else:
            return '^'
    if direc == '^':
        if track == '/':
            return '>'
        else:
            return '<'
    if direc == 'v':
        if track == '/':
            return '<'
        else:
            return '>'


def cross_intersection(direc, turn_num):
    if direc == '>':
        return ('^', '>', 'v')[turn_num]
    if direc == '<':
        return ('v', '<', '^')[turn_num]
    if direc == '^':
        return ('<', '^', '>')[turn_num]
    if direc == 'v':
        return ('>', 'v', '<')[turn_num]


class cart:
    def __init__(self, x_in, y_in, direction_in, map_in):
        self.x = x_in
        self.y = y_in
        self.direction = direction_in
        self.map = map_in
        self.turn_num = 0
        self.evolved = None

    def evolve_step(self):
        to_move = direction_dict[self.direction]
        self.x += to_move[0]
        self.y += to_move[1]
        if self.map[self.y][self.x] in ['-', '|']:
            return
        if self.map[self.y][self.x] in ['/', '\\']:
            self.direction = turn_corner(self.direction, self.map[self.y][self.x])
            return
        self.direction = cross_intersection(self.direction, self.turn_num)
        self.turn_num = (self.turn_num + 1) % 3

    def cart_order(self):
        return self.y*len(self.map[0]) + self.x

    def get_coords(self):
        return (self.x, self.y)


class railway:
    def __init__(self, map_in, carts_in):
        self.map = map_in
        self.carts = carts_in
        self.crashed = False
        self.carts = sorted(self.carts, key=lambda x: x.cart_order())

    def check_crash(self):
        coords = set()
        for cart in self.carts:
            coord = cart.get_coords()
            if coord in coords:
                return coord
            coords.add(coord)
        return None

    def remove_crashed_carts(self):
        coord = self.check_crash()
        if coord is None:
            return
        for i in range(len(self.carts)-1, -1, -1):
            if self.carts[i].get_coords() == coord:
                self.carts.pop(i)
        self.remove_crashed_carts()


    def evolve_step(self, stop_at_crash, new_step=True):
        if new_step:
            self.carts = sorted(self.carts, key=lambda x: x.cart_order())
            for cart in self.carts:
                cart.evolved = False
        for cart in self.carts:
            if cart.evolved:
                continue
            cart.evolve_step()
            cart.evolved = True
            crash = self.check_crash()
            if crash is not None:
                self.crashed = True
                if stop_at_crash:
                    return
                self.remove_crashed_carts()
                self.evolve_step(False, False)

    def __str__(self):
        rval = ''
        carts_to_show = {}
        for cart in self.carts:
            carts_to_show[(cart.x, cart.y)] = cart.direction
        for y, line in enumerate(self.map):
            rval_line = ''
            for x, char in enumerate(self.map[y]):
                if (x, y) in carts_to_show:
                    rval_line += carts_to_show[(x, y)]
                    continue
                rval_line += self.map[y][x]
            rval += rval_line + '\n'
        return rval


def part1(filename):
    map, carts = readfile(filename)
    my_railway = railway(map, carts)
    while not my_railway.crashed:
        my_railway.evolve_step(True)
    print("The coordinates of the first crash are {}".format(my_railway.check_crash()))


def part2(filename):
    map, carts = readfile(filename)
    my_railway = railway(map, carts)
    while len(my_railway.carts) != 1:
        my_railway.evolve_step(False)
    print("The coordinates of the final cart are {}".format(my_railway.carts[0].get_coords()))


if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_13.dat")
    timer.checkpoint_hit()
    part2("data/day_13.dat")
    timer.checkpoint_hit()
    timer.end_hit()
