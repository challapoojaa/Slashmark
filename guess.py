import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    number = random.randint(1, 200)
    guesses_taken = 0

    while guesses_taken < 6:
        time.sleep(0.25)
        try:
            guess = int(input("Guess: "))

            if 1 <= guess <= 200:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("Too low!")
                    elif guess > number:
                        print("Too high!")
                    else:
                        print("Try Again!")

                if guess == number:
                    break

            else:
                print("Please enter a number between 1 and 200")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guesses_taken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}')

play_again = "yes"

while play_again.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again?")
    play_again = input()
