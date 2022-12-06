#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 2, Part B. Advent Of Code 2021 ###


# Read input from file
with open('input.txt') as f:
    pos_changes = [line.strip() for line in f]
# Splitting direction instructions into pairs [direction, stepsize]
pos_pairs = [key.split(' ') for key in pos_changes]

horizontal_pos = 0
depth_pos = 0
aim = 0

for pair in pos_pairs:
    if pair[0] == 'down':
        aim += int(pair[1])
    elif pair[0] == 'up':
        aim -= int(pair[1])
    elif pair[0] == 'forward':
        horizontal_pos += int(pair[1])
        depth_pos += (aim * int(pair[1]))

sol = depth_pos * horizontal_pos
print(f'Day2b answer: {sol}')



