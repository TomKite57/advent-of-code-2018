# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

import numpy as np

FILENAME = "day_1_data.dat"


if __name__ == "__main__":
    data = np.genfromtxt(FILENAME, dtype='int32')
    all_freqs = np.zeros(1, dtype='int32')

    current_index = 0
    total_iterations = 0

    while True:
        if (current_index >= len(data)):
            current_index = 0
        new_freq = all_freqs[-1] + data[current_index]

        if new_freq in all_freqs:
            print("Yay!")
            print("First repeated frequency is {}".format(new_freq))
            print("This took {} iterations".format(total_iterations))
            break

        all_freqs = np.append(all_freqs, new_freq)
        current_index += 1
        total_iterations += 1
