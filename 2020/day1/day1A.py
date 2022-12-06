#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: laffe12
"""

### Day 1, Part A. Advent Of Code 2020 ###

with open("input.txt", "r") as f:
	lines = [line.strip("\n") for line in f.readlines()]

for x in lines:
	for y in lines:
		if int(x) + int(y) == 2020:
			print(int(x)*int(y))