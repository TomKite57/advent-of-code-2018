# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:48 2020

@author: mbcx4tk5
"""

total_count = 0
current_pos = 0


def readfile(filename):
    # Get raw data from file
    with open(filename) as file:
        line = [line.strip() for line in file][0]

    # interpret each line as two CSV ints
    data = [int(x) for x in line.split(' ')]
    return data


def process_class(code):
    global total_count, current_pos
    current_pos += 2
    meta_data_num = code[current_pos-1]
    for _ in range(code[current_pos-2]):
        process_class(code)
    for _ in range(meta_data_num):
        total_count += code[current_pos]
        current_pos += 1
    return


if __name__ == "__main__":
    data = readfile("day_8_data.dat")
    process_class(data)

    print("The total sum of metadata is {}.".format(total_count))
