# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:35:43 2020

@author: mbcx4tk5
"""

import numpy as np

FILENAME = "day_1_data.dat"


if __name__ == "__main__":
    data = np.genfromtxt(FILENAME, dtype='int32')
    total_sum = sum(data)
    print("Total sum is {}".format(total_sum))
