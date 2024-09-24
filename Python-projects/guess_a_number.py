import random

computer_number = random.randint(1,100)
print("Welcome to guess the number game!\nTry to guess from 1 to 100 the given number.")
player_number = 0

while player_number != computer_number:
    guess = input("You choose the number ")

    if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
        raise SystemExit("Invalid input.\nTry again in a few minutes.")

    player_number = int(guess)

    if player_number == computer_number:
        print("You guess it BRAVO!")
    elif player_number < computer_number:
        print("Too Low!")
    elif player_number > computer_number:
        print("Too High!")
    else:
        print("You're unlucky...\nTry again.")