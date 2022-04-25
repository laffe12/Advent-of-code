import numpy as np

with open('diagnostic_input.txt') as f:
	input_binary = [line.strip() for line in f.readlines()]

gamma = []
epsilon = []
binary_matrix = []

# Coverting numbers to int and creating an input matrix
for string in input_binary:
	char_list = [int(char) for char in string]
	binary_matrix.append(char_list)

# Matrix transpose  
binary_matrix = np.array(binary_matrix)
binary_matrix = binary_matrix.transpose()

# Counting zeroes and ones 
for row in binary_matrix:
	zero_count = 0
	one_count = 0

	for number in row:
		if number == 0:
			zero_count += 1

		elif number == 1:
			one_count += 1

	if one_count > zero_count:
		gamma.append(1)
		epsilon.append(0)
	elif zero_count > one_count:
		gamma.append(0)
		epsilon.append(1)

# Covert list of binary numbers to int
gamma_int = int(''.join(str(i) for i in gamma),2)
epsilon_int = int(''.join(str(i) for i in epsilon),2)


print(f'Solution day 3a: {gamma_int * epsilon_int}')
