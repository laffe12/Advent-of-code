#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:34:16 2022

@author: laffe
"""

with open("input.txt") as f:
	lines = [line.strip("\n") for line in f.readlines()]

password_policies = [line.split() for line in lines]
valid_password_count = 0

def validate_password(pos1, pos2, character, password):
    
    if password[pos1] == character:
        if password[pos2] == character:
            return False
        elif password[pos2] != character:
            return True
        else: 
            return False
    elif password[pos2] == character:
        if password[pos1] == character:
            return False
        elif password[pos1] != character:
            return True
        else: 
            return False
        
    
for policy in password_policies:
    char_range = policy[0].split('-')
    min = int(char_range[0])-1
    max = int(char_range[1])-1
    
    char = policy[1].replace(":", "")
    password = policy[2]
    
    valid_check = validate_password(pos1=min, pos2=max, 
                                    character=char, password=password)
    print(valid_check)
    if valid_check:
        valid_password_count +=1
        
print(valid_password_count)