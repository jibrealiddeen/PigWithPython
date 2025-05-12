import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll 

while True: 
    print("Hello, you! Must be between 2 - 4 players to play Cold's mini game! \n===============================================================")
    players = input("Enter the number of players (2 - 4):  ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break 
        else:
            print("Remember, must be between 2 - 4 players!")
    else: 
        print("Invalid! Did you read the rule??")

max_score = 50 
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_idx in range(players):
        current_score = 0 


        should_roll = input("Would you like to roll? (Y/N) ").lower()
        
        if should_roll == "y":
            value = roll()
            if value ==1:
                print("You rolled a 1! Turn done!")
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your socre is:", current_score)

            
        elif should_roll == "n":
            break




