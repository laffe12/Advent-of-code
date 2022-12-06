#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 3, Part A. Advent Of Code 2022 ###

with open('input.txt') as file:
    input = file.readlines()
    
items = [x.strip("\n") for x in input]  # remove "\n"

### Priority template ###
lower_case_priorities = "abcdefghijklmnopqrstuvwxyz"
upper_case_priorities = lower_case_priorities.upper()
priorities = lower_case_priorities + upper_case_priorities

sum = 0
for item in items:
    
    # Split the string in half
    length = len(item)
    first_item = [item[s] for s in range(0, int(length/2))]
    second_item = [item[z] for z in range(int(length/2), length)]
    
    # Find common items in both strings
    common_items = [c for c in first_item if c in second_item]
    
    # Matching the priority to common item and adding points (+ 1 point extra
    # if a match is found)
    for i in range(0, len(priorities)):
        if priorities[i] == common_items[0]:
            sum += i + 1
            
print(f'Answer A: {sum}')
            
    
    

    

