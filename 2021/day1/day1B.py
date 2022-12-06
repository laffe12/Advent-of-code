#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 1, Part B. Advent Of Code 2021 ###

import numpy as np
# Read input from file
with open('input_depth.txt') as f:
    depths = f.readlines()

# Convert depths to int
depths_values = [int(x) for x in depths]

# Realizing that instead of using a typical sliding window, one can just compare 1st and 4th, 4th and 7th and so on.
# The 2 "inner" numbers of the sliding window doesnt change
# Previous solution uses a sliding window of one, here we choose three instead
increase_counter = 0
for i in range(3,len(depths_values)):
    if depths_values[i] > depths_values[i-3]:
        increase_counter += 1

print(f'Day1b solution {increase_counter}')

