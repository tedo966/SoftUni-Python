import random

rock = "ROCK"
paper = "PAPER"
scissors = "SCISSORS"

game_rule = print("You are about to start <-rock->  <-scissors->  <-paper-> game!\n"
                  "Please choose smart!\nYou must input: \n(r) for Rock \n(c) for Scissors \n(p) for Paper\n ")
player_move = input("Choose [R]ock, [P]aper or [S]cissors: ")

if player_move.lower() == "r":
    player_move = rock
    print(f"You chose {player_move}")
elif player_move.lower() == "c":
    player_move = scissors
    print(f"You chose {player_move}")
elif player_move.lower() == "p":
    player_move = paper
    print(f"You chose {player_move}")
else:
    raise SystemExit("Invalid Input. Try again...") #exits the whole program with red message
print()
print("Now it's time for the computer to choose...")
print()
computer_random_num = random.randint(1,3) # makes computer choose random num between 1-3
computer_move = ""
if computer_random_num.__str__() == "1":
    computer_move = "ROCK"
    print(f"Computer chooses:\n{computer_move}")
elif computer_random_num.__str__() == "2":
    computer_move = "SCISSORS"
    print(f"Computer chooses:\n{computer_move}")
elif computer_random_num.__str__() == "3":
    computer_move = "PAPER"
    print(f"Computer chooses:\n{computer_move}")

if player_move == "ROCK" and computer_move == "SCISSORS" \
        or player_move == "PAPER" \
        and computer_move == "ROCK" \
        or player_move == "SCISSORS" \
        and computer_move == "PAPER":
    print()
    print("Congrats!\nYou win the game!!!")
elif computer_move == "ROCK" and player_move == "SCISSORS" \
        or computer_move == "PAPER" \
        and player_move == "ROCK" \
        or computer_move == "SCISSORS" \
        and computer_move == "PAPER":
    print()
    print("Ohh craps...\nYou've lost the battle buddy...\nTry again.")
elif player_move == computer_move:
    print()
    print("So what do we have here?\nDRAW!?\nGo again.")


