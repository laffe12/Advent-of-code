# Read input from file
with open('input_depth.txt') as f:
    depths = f.readlines()

# Convert depths to int
depths_values = [int(x) for x in depths]

# if depth is increased, add 1 to counter
increase_counter = 0
for i in range(1,len(depths_values)):
    if depths_values[i] > depths_values[i-1]:
        increase_counter += 1

print(f'Day1a solution {increase_counter}')

