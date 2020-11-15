# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 13:32:29 2020

@author: mbcx4tk5
"""

def valid_reac(a, b):
    if a == a.lower():
        if b == a.upper():
            return True
    else:
        if b == a.lower():
            return True
    return False


class polymer():
    def __init__(self, code_in):
        self.code = code_in
        self.simplified = False

    def react(self):
        for i in range(len(self.code)-2, -1, -1):
            if valid_reac(self.code[i], self.code[i+1]):
                self.code = self.code[:i] + self.code[i+2:]
                return
        self.simplified = True
        return

    def full_react(self):
        while not self.simplified:
            self.react()
        return

    def get_length(self):
        return len(self.code)

    def get_unit_types(self):
        rval = []
        for i in range(len(self.code)):
            unit = self.code[i].lower()
            if unit not in rval:
                rval.append(unit)
        return rval

    def remove_unit(self, unit):
        i = 0
        while i < len(self.code):
            if self.code[i].lower() == unit:
                self.code = self.code[:i] + self.code[i+1:]
                continue
            i += 1


if __name__ == "__main__":
    data = open("day_5_data.dat").readline()
    my_pol = polymer(data)
    my_pol.full_react()
    
    all_units = my_pol.get_unit_types()
    unit_length_dict = {}

    for unit in all_units:
         unit_length_dict[unit] = polymer(my_pol.code)
         unit_length_dict[unit].remove_unit(unit)
         unit_length_dict[unit].full_react()
    
    max_unit = min(unit_length_dict.keys(),
                   key = lambda x: unit_length_dict[x].get_length())
    print("The shortest length is found by removing {}/{}, with length {}"
          .format(max_unit,
                  max_unit.upper(),
                  unit_length_dict[max_unit].get_length()))