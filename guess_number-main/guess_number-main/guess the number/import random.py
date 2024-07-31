import random
import time

def generate_number():
    return random.randint(1, 200)

def get_player_name():
    print("May I ask you for your name?")
    return input().strip()

def intro(name):
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def get_player_guess():
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if 1 <= guess <= 200:
                return guess
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
        except ValueError:
            print("I don't think that is a number. Please enter a valid number.")

def play_game():
    number = generate_number()
    guesses_taken = 0
    max_guesses = 6

    while guesses_taken < max_guesses:
        time.sleep(0.25)
        guess = get_player_guess()
        guesses_taken += 1
        
        if guess < number:
            print("The guess of the number that you have entered is too low.")
        elif guess > number:
            print("The guess of the number that you have entered is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            return
        
        if guesses_taken < max_guesses:
            time.sleep(0.5)
            print("Try Again!")

    print(f"Nope. The number I was thinking of was {number}.")

def main():
    playagain = "yes"
    while playagain.lower() in ("yes", "y"):
        global name
        name = get_player_name()
        intro(name)
        play_game()
        print("Do you want to play again?")
        playagain = input().strip()

if __name__ == "__main__":
    main()
