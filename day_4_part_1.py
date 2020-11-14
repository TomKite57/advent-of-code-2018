# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:53:38 2020

@author: mbcx4tk5
"""

import numpy as np


class time_stamp():
    def __init__(self, time_str):
        self.year, self.month, self.day = np.array(time_str[:10].split('-'),
                                                   dtype='int')
        self.hour, self.minute = np.array(time_str[11:].split(':'),
                                          dtype='int')
        self.date = np.array([self.year, self.month, self.day,
                              self.hour, self.minute])

    def total_minutes(self):
        time = (((self.year - 1518)*12 + self.month)*31 + self.day)*24
        time = (time + self.hour)*60 + self.minute
        return time

    def __eq__(self, other):
        return all(self.date == other.date)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        less_than = self.date < other.date
        greater_than = self.date > other.date
        for i in range(len(self.date)):
            if less_than[i]:
                return True
            elif greater_than[i]:
                return False
        return False

    def __gt__(self, other):
        return not (self == other or self < other)

    def __le__(self, other):
        return (self < other or self == other)

    def __ge__(self, other):
        return (self > other or self == other)


class guard():
    def __init__(self, ID_in):
        self.ID = ID_in
        self.minute_count = np.zeros(60, dtype='int')

    def add_time(self, sleep_time, wake_time):
        try:
            for num in range(sleep_time.minute, wake_time.minute):
                self.minute_count[num] += 1
        except AttributeError:
            return

    def total_time(self):
        return self.minute_count.sum()

    def best_minute(self):
        max_val = max(self.minute_count)
        return int(np.where(self.minute_count == max_val)[0])


def split_input_line(line):
    time_substr = line[line.find('[')+1:line.find(']')]
    event_substr = line[line.find(']')+2:]
    return time_substr, event_substr


def process_event(line):
    if line.count('wakes'):
        return 'wake'
    if line.count('falls'):
        return 'sleep'
    split = line.split(' ')
    for sub_str in split:
        if sub_str.find('#') != -1:
            return int(sub_str[1:])


def read_data(filename):
    output_data = np.empty((0,2))
    with open(filename) as input_file:
        raw_data = [x.strip() for x in input_file]
    for row in raw_data:
        time_str, event = split_input_line(row)
        new_row = np.array([time_stamp(time_str), process_event(event)])
        output_data = np.vstack((output_data, new_row))
    return sorted(output_data, key=lambda x: x[0])


if __name__ == "__main__":
    data = read_data("day_4_data.dat")
    guard_index = {}

    current_ID = data[0][1]
    sleep_time = None
    wake_time = None
    counter = 0
    for line in data:
        if line[1] == 'sleep':
            sleep_time = line[0]
        elif line[1] == 'wake':
            wake_time = line[0]
            if current_ID not in guard_index:
                guard_index[current_ID] = guard(current_ID)
            guard_index[current_ID].add_time(sleep_time, wake_time)
        else:
            current_ID = line[1]


    max_ID = max(guard_index.keys(), key=lambda x: guard_index[x].total_time())
    print("Puzzle solution is {}"
          .format(guard_index[max_ID].best_minute()*max_ID))
