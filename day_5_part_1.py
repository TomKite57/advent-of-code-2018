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
                

if __name__ == "__main__":
    data = open("day_5_data.dat").readline()
    my_pol = polymer(data)
    my_pol.full_react()
    print("The length after reacting is {}".format(my_pol.get_length()))