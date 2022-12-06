### Day 2 2022 Advent Of Code ###
with open('input.txt') as file:
    input_list = file.readlines()

rounds = [x.split() for x in input_list]
score = 0
for round in rounds:
    opponents_choice = round[0]
    players_choice = round[1]
    
    ## Player plays X = ROCK
    if players_choice == "X": #ROCK
        score += 1  # 1 point for playing rock
        
        if opponents_choice == "A": #ROCK
            # Draw gives 3 points
            score += 3
        elif opponents_choice == "B": #PAPER
            # Paper beats rock, player wins
            score += 0
        elif opponents_choice == "C": #SCISSORS
            # Rock beats scissors
            score += 6
            
    ## Player plays Y = PAPER
    if players_choice == "Y": #PAPER
        score += 2  # 2 point for playing paper
            
        if opponents_choice == "A": #ROCK
        # Paper beats rock, win
            score += 6
        elif opponents_choice == "B": #PAPER
            # Draw
            score += 3
        elif opponents_choice == "C": #SCISSORS
        # Scissors beats paper, loss
            score += 0
            
    ## Player plays Z = SCISSORS
    if players_choice == "Z": #SCISSORS
        score += 3  # 2 point for playing paper
                
        if opponents_choice == "A": #ROCK
            # Rock beats scissors, loss
            score += 0
        elif opponents_choice == "B": #PAPER
            # Scissors beats paper, win
            score += 6
        elif opponents_choice == "C": #SCISSORS
            # Draw
            score += 3
         
print(f'Answer A: {score}')


score = 0
for round in rounds:
    opponents_choice = round[0]
    result = round[1]
    
    ## Need a loss = X
    if result == "X": #LOSS
        
        if opponents_choice == "A": #ROCK
            # Scissors loses to rock
            score += 3
        elif opponents_choice == "B": #PAPER
            # Rock loses to paper
            score += 1
        elif opponents_choice == "C": #SCISSORS
            # Paper loses to scissors
            score += 2
            
    ## Need a draw = Y
    if result == "Y": #DRAW
        score += 3  # 3 point for a draw
            
        if opponents_choice == "A": #ROCK
            # 1 point for playing rock
            score += 1
        elif opponents_choice == "B": #PAPER
            # 2 point for playing paper
            score += 2
        elif opponents_choice == "C": #SCISSORS
            # 3 point for playing scissors
            score += 3
            
    ## Need a win = Z
    if result == "Z": #WIN
        score += 6  # 6 point for a win
                
        if opponents_choice == "A": #ROCK
            # Paper wins against rock
            score += 2
        elif opponents_choice == "B": #PAPER
            # Scissors wins against paper
            score += 3
        elif opponents_choice == "C": #SCISSORS
            # Rock wins against scissors
            score += 1
print(f'Answer B: {score}')
        
    
