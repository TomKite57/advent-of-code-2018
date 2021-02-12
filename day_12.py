# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:50:22 2020

@author: TKite
"""

from copy import deepcopy


first_ind = 0
prev_states = []
indices = []


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    initial_condition = lines[0].strip('initial state: ')
    rules = [line.split(' => ') for line in lines[2:]]
    rule_dict = {}
    for r in rules:
        rule_dict[r[0]] = r[1]
    return initial_condition, rule_dict


def plants_to_int(plants):
    binary = plants.replace('.', '0')
    binary = binary.replace('#', '1')
    return int(binary, 2)


def adapt_row(plants):
    global first_ind
    # Expand on left
    while '#' in plants[:3]:
        plants = '.' + plants
        first_ind -= 1
    # Contract on left
    while '#' not in plants[:4]:
        plants = plants[1:]
        first_ind += 1
    # Expand on right
    while '#' in plants[-3:]:
        plants = plants + '.'
    # Contract on right
    while '#' not in plants[-4:]:
        plants = plants[:-1]
    return plants


def evolve_plants(plants, rules):
    new_plants = '..'
    for i in range(2, len(plants)-2):
        new_plants += rules[plants[i-2:i+3]]
    new_plants += '..'
    new_plants = adapt_row(new_plants)
    return new_plants


def count_after_N_steps(initial_cond, steps):
    plants = adapt_row(deepcopy(initial_cond))
    global first_ind, prev_states, indices
    first_ind = 0
    prev_states = [plants_to_int(plants)]
    indices.append(first_ind)

    i = 1
    while i <= steps:
        i += 1
        plants = evolve_plants(plants, rule_dict)
        state_int = plants_to_int(plants)
        if state_int in prev_states:
            ind = prev_states.index(state_int)
            old_first_ind = indices[ind]
            first_ind += (first_ind - old_first_ind)*((steps-i)//(i-ind))
            for _ in range((steps-i) % (i-ind)):
                plants = evolve_plants(plants, rule_dict)
            break
        else:
            prev_states.append(state_int)
            indices.append(first_ind)

    return sum([i+first_ind for i, p in enumerate(plants) if p == '#'])


if __name__ == "__main__":
    initial_cond, rule_dict = readfile("day_12_data.dat")
    initial_cond = adapt_row(initial_cond)

    #print("Part 1:")
    #total_sum = count_after_N_steps(initial_cond, 20)
    #print("Total index sum: {}.".format(total_sum))

    print("Part 2:")
    total_sum = count_after_N_steps(initial_cond, 50000000000)
    print("Total index sum: {}.".format(total_sum))
