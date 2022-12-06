#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 4, Part B. Advent Of Code 2022 ###


with open('input.txt') as file:
    input = file.readlines()
    
pairs = [x.strip("\n") for x in input]  # remove "\n"
pairs = [x.split(",") for x in pairs]
longest_list = []
shortest_list = []
overlaps = 0

for pair in pairs:
    
    first_pair = pair[0].split("-")
    second_pair = pair[1].split("-")
    
    first_pair = [int(first_pair[0]), int(first_pair[1])+1]
    second_pair = [int(second_pair[0]), int(second_pair[1])+1]
    
    first_range = [x for x in range(first_pair[0], first_pair[1])]
    second_range = [x for x in range(second_pair[0], second_pair[1])]
    
    if len(first_range) >= len(second_range):
        shortest_list = second_range
        longest_list = first_range
    else:
        shortest_list = first_range
        longest_list = second_range
        
    common_items = [c for c in shortest_list if c in longest_list]
    if len(common_items) > 0:
        overlaps +=1
        
print(f"Answer 4B: {overlaps}")

    

