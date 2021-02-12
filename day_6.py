# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:48 2020

@author: mbcx4tk5
"""

from aoc_tools import Advent_Timer


def readfile(filename):
    # Get raw data from file
    with open(filename) as file:
        lines = [line.strip() for line in file]

    # interpret each line as two CSV ints
    data = [[int(x) for x in line.split(',')] for line in lines]
    return data


def manhat_dist(a, b):
    return sum([abs(b[i] - a[i]) for i in range(len(a))])


def unique_min(points, pos):
    dists = [manhat_dist(p, pos) for p in points]
    min_val = min(dists)
    if dists.count(min_val) == 1:
        return points[dists.index(min_val)]
    else:
        return None


def full_dist(points, pos):
    count = 0
    for p in points:
        count += manhat_dist(p, pos)
    return count


def part1(filename):
    # Read data
    points = readfile(filename)

    # Make lists for area tallies and valid points
    areas = [0 for _ in points]
    inf = [0 for _ in points]

    # Find extreme coords for perimiter
    x_max = max([p[0] for p in points])
    x_min = min([p[0] for p in points])
    y_max = max([p[1] for p in points])
    y_min = min([p[1] for p in points])

    # Add up areas within largest perimiter
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            closest_point = unique_min(points, [x, y])
            if closest_point is not None:
                areas[points.index(closest_point)] += 1

    # Go around perimiter finding which points are infinite
    for x in range(x_min, x_max+1):
        for y in (y_min, y_max):
            closest_point = unique_min(points, [x, y])
            if closest_point is None:
                continue
            ind = points.index(closest_point)
            inf[ind] = 1

    # And again...
    for y in range(y_min+1, y_max):
        for x in (x_min, x_max):
            closest_point = unique_min(points, [x, y])
            if closest_point is None:
                continue
            ind = points.index(closest_point)
            inf[ind] = 1

    # Find best index. Metric sets = 0 if point is inf
    best_index = max(range(len(points)),
                     key=lambda i: areas[i]*(1-inf[i]))

    print("The best point is {} with an area of {}."
          .format(points[best_index], areas[best_index]))

def part2(filename):
    # Read data
    points = readfile(filename)

    # Find extreme coords for perimiter
    x_max = max([p[0] for p in points])
    x_min = min([p[0] for p in points])
    y_max = max([p[1] for p in points])
    y_min = min([p[1] for p in points])

    area_count = 0

    # Add up areas within largest perimiter
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if full_dist(points, [x, y]) < 10000:
                area_count += 1

    print("The area with less than 10000 distance is {}.".format(area_count))

if __name__ == "__main__":
    timer = Advent_Timer()
    part1("data/day_6.dat")
    timer.checkpoint_hit()
    part2("data/day_6.dat")
    timer.checkpoint_hit()
    timer.end_hit()
