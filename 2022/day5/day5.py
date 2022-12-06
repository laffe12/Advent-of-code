#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 5, Part A & B. Advent Of Code 2022 ###

# Manually entering stack input
stack = [['B', 'W', 'N'],
        ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
        ['Q', 'H', 'Z', 'W', 'R'],
        ['W', 'D', 'V', 'J', 'Z', 'R'],
        ['S', 'H', 'M', 'B'],
        ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
        ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
        ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
        ['Z', 'W', 'M', 'S', 'C', 'D', 'J']]


# Read input from file
with open('input.txt') as f:
    input = f.readlines()

# remove new line from input    
procedures = [x.strip("\n") for x in input]

for i in range(0, len(procedures)):
    # split the input
    split_strings = procedures[i].split(" ")
    number_of_boxes = int(split_strings[1])
    from_list = int(split_strings[3]) - 1 # move boxes from list with this index 
    to_list = int(split_strings[5]) - 1 # move boxes to list with this index 
    length_of_list = len(stack[from_list])  # length of the "from"-list
    
    # determine which boxes should be moved
    boxes_to_move = stack[from_list][length_of_list - number_of_boxes:]
    
    #boxes_to_move.reverse() # uncomment this for part 1 solution
    
    # place the boxes on top of target pile (to_list)
    for j in range(0, len(boxes_to_move)):
        stack[to_list].append(boxes_to_move[j])
    # remove the boxes from the previous stack    
    stack[from_list] = stack[from_list][:-number_of_boxes]
    
result = ""
for i in range(0, len(stack)):
    result += stack[i][-1]
print(result)
    