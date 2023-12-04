"""
Adam Rosén
"""


# Reading the input-file
with open('input.txt') as f:
    input = f.readlines()

# Removes newline (\n) and split rows into list elements
input_list = [x.strip("\n") for x in input]


sum = 0 #declaring sum variable
number_string = '' # declaring an empty string

# for every string in input, go through each individual character for each string and and check the character is numeric. If it is a number, save it
for string in input_list:
    number_string = ''
    for character in string:
        if character.isnumeric():
            number_string += character
            
    number = int(number_string[0] + number_string[-1])
    sum += number
            
print(f'Answer day1a: {sum}')



    

