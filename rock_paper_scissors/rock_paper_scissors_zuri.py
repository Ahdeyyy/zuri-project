import random
choice = ["R", "P", "S"]
choices = {
    "R":"ROCK",
    "P":"PAPER",
    "S":"SCISSORS"
    }

print("""
R = rock
P = paper
S = scissors

""") 

while True:
    player_choice = str(input()).upper()
    ai_choice = random.choices(choice)
    
    if not player_choice in choice:
        print("enter R , P or S")
        continue 
    print(f"Player({choices[player_choice]}) : CPU({choices[ai_choice[0]]}) ")
    
    if player_choice == ai_choice[0]:
        print("DRAW")
    elif player_choice == 'R' and ai_choice[0] == 'S':
        print("Player Wins")
        break
    elif player_choice == 'S' and ai_choice[0] == 'P':
        print("Player Wins")
        break
    elif player_choice == 'P' and ai_choice[0] == 'R':
        print("Player Wins")
        break
    else:
        print("Computer wins")
        break
