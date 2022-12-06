with open("input.txt") as f:
	lines = [line.strip("\n") for line in f.readlines()]

password_policies = [line.split() for line in lines]
valid_password_count = 0

def validate_password(min, max, character, password):
    char_count = password.count(character)
    if min <= char_count <= max:
        return True
    else:
        return False
    
for policy in password_policies:
    char_range = policy[0].split('-')
    min = int(char_range[0])
    max = int(char_range[1])
    
    char = policy[1].replace(":", "")
    password = policy[2]
    
    valid_check = validate_password(min=min, max=max, 
                                    character=char, password=password)
    print(valid_check)
    if valid_check:
        valid_password_count +=1
        
print(valid_password_count)
    

