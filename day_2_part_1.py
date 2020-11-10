# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

import numpy as np

FILENAME = "day_2_data.dat"


def N_letters(my_str, N):
    for char in my_str:
        if my_str.count(char) == N:
            return True
    return False


if __name__ == "__main__":
    data = np.genfromtxt(FILENAME, dtype='str')
    two_num = np.empty((0, 0), dtype='int8')
    three_num = np.empty((0, 0), dtype='int8')

    for line in data:
        two_num = np.append(two_num, N_letters(line, 2))
        three_num = np.append(three_num, N_letters(line, 3))

    checksum = sum(two_num) * sum(three_num)

    print("The checksum is {}".format(checksum))
