# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

import numpy as np

FILENAME = "day_2_data.dat"


def letter_diff(str1, str2):
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
    return diff_count


def remove_diff(str1, str2):
    if letter_diff(str1, str2) != 1:
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return str1[:i] + str1[i+1:]


if __name__ == "__main__":
    data = np.genfromtxt(FILENAME, dtype='str')

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            rval = remove_diff(data[i], data[j])
            if rval:
                print("Found it! The answer is\n" + rval)
