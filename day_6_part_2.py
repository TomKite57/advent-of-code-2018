# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:48 2020

@author: mbcx4tk5
"""


def readfile(filename):
    # Get raw data from file
    with open(filename) as file:
        lines = [line.strip() for line in file]

    # interpret each line as two CSV ints
    data = [[int(x) for x in line.split(',')] for line in lines]
    return data


def manhat_dist(a, b):
    return sum([abs(b[i] - a[i]) for i in range(len(a))])


def full_dist(points, pos):
    count = 0
    for p in points:
        count += manhat_dist(p, pos)
    return count


if __name__ == "__main__":
    # Read data
    points = readfile("day_6_data.dat")

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
