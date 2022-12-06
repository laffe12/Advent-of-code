#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 1, Part A & B. Advent Of Code 2022 ###

with open('input.txt') as file:
    calories = file.readlines()

sum_list = []
calorie_sum = 0
    
for i in range(0,len(calories)):
    if calories[i] == "\n":
        sum_list.append(calorie_sum)
        calorie_sum = 0
        i += 1
    else:
        calorie_sum += int(calories[i])
        
sorted_list = sorted(sum_list)

print(f'Answer A: {max(sum_list)}')
print(f'Answer B: {sum(sorted_list[-3:])}')