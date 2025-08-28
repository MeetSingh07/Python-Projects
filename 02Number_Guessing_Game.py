# Number Guessing Game

import random

random_number=random.randint(1,99)

print("Computer Choosed The Number")

loop="running"

number_of_guesses=0

while loop=="running":
    guess=int(input("Guess the number between 1 - 99 : "))
    number_of_guesses=number_of_guesses+1

    if guess<1 or guess>99:
        print("Choose between 1-99")
    elif number_of_guesses>=99:
        print("Game Over...No more attempts left")
        loop="end"
    elif guess>random_number:
        print("Choose a lower number.")
    elif guess<random_number:
        print("Choose a higher number.")
    else:
        print("Congratulations...You Guessed the Number")
        print(f"Number of Guesses = {number_of_guesses}")
        loop="end"

f = open("score.txt", "r+")

score_str = str(number_of_guesses)

if number_of_guesses >= 10:
    f.seek(44)
    f.write(score_str[0])   # first digit
    f.seek(45)
    f.write(score_str[1])   # second digit
else:
    f.seek(44)
    f.write("0")            # pad with zero
    f.seek(45)
    f.write(score_str)      # actual digit

f.close()