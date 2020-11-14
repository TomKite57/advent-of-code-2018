# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

import numpy as np


class cloth_cut():
    def __init__(self, in_code):
        self.ID, self.x, self.y, self.Lx, self.Ly = read_ID_string(in_code)

    def __str__(self):
        return "ID: {}, x: {}, y: {}, Lx: {}, Ly: {}".format(
            self.ID, self.x, self.y, self.Lx, self.Ly)

    def max_x(self):
        return self.x + self.Lx

    def max_y(self):
        return self.y + self.Ly

    def apply_cut(self, cloth):
        for i in range(self.x, self.max_x()):
            for j in range(self.y, self.max_y()):
                cloth[j, i] += 1
        return cloth

    def independent_cut(self, full_cloth):
        for i in range(self.x, self.max_x()):
            for j in range(self.y, self.max_y()):
                if cloth[j, i] != 1:
                    return False
        return True


def read_ID_string(str_in):
    ID = str_in[0][1:]
    x, y = str_in[2].split(',')
    y = y[:-1]
    Lx, Ly = str_in[3].split('x')
    return np.array([ID, x, y, Lx, Ly], dtype='int32')


def total_size(cloth_cut_list):
    max_x = max([cut.max_x() for cut in cloth_cut_list])
    max_y = max([cut.max_y() for cut in cloth_cut_list])
    return max_x, max_y


if __name__ == "__main__":
    input_data = np.genfromtxt("day_3_data.dat", dtype="str", comments=None)
    cloth_cut_list = [cloth_cut(x) for x in input_data]
    max_x, max_y = total_size(cloth_cut_list)

    cloth = np.zeros((max_y, max_x))
    for cut in cloth_cut_list:
        cloth = cut.apply_cut(cloth)

    solution_cut = None

    for cut in cloth_cut_list:
        if cut.independent_cut(cloth):
            solution_cut = cut

    print("The independent cut has ID = {}".format(solution_cut.ID))
