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

    def total_tree_meta(self):
        meta = sum(self.metadata)
        for child in self.children:
            meta += child.total_tree_meta()
        return meta


if __name__ == "__main__":
    data = readfile("day_8_data.dat")
    tree = node(data)
    total_count = tree.total_tree_meta()

    print("The total sum of metadata is {}.".format(total_count))
