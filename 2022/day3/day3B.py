
with open('input.txt') as file:
    input = file.readlines()
    
items = [x.strip("\n") for x in input]  # remove "\n"

### Priority template ###
lower_case_priorities = "abcdefghijklmnopqrstuvwxyz"
upper_case_priorities = lower_case_priorities.upper()
priorities = lower_case_priorities + upper_case_priorities

sum = 0

### Check groups of three
for i in range(0,len(items),3):
    
    ### Check common items in first and second string.
    ### and save the common items in a list. Then compare it with third string.
    common_12 = [c for c in items[i] if c in items[i+1]]
    common_3 = [c for c in common_12 if c in items[i+2]]
    
    ### Check the common item and give points
    for i in range(0, len(priorities)):
        if priorities[i] == common_3[0]:
            sum += i + 1


            
    
    
print(f'Answer 3B: {sum}')
    

