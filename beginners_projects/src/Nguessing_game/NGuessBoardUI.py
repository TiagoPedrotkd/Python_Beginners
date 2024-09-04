import random
import math
import time
from colorama import Fore, Style, init

init(autoreset=True)

class NGuessBoardUI:

    def __init__(self):
        print(Fore.CYAN + "\nWelcome to the Guessing Game!")
        print(Fore.CYAN + "You need to guess the correct number within a range.")

        self.choose_game_mode()

    def choose_game_mode(self):
        print(Fore.CYAN + "\nAvailable Game Modes:")
        print(Fore.CYAN + "1. Classic Mode - Guess the number with limited attempts.")
        print(Fore.CYAN + "2. Time Challenge Mode - Guess the number before time runs out.")
        print(Fore.CYAN + "3. Infinite Mode - Keep playing until you guess correctly or quit.")

        choice = input(Fore.YELLOW + "Select the game mode (1, 2, or 3): ")

        if choice == '1':
            self.classic_mode()
        elif choice == '2':
            self.time_challenge_mode()
        elif choice == '3':
            self.infinite_mode()
        else:
            print(Fore.RED + "Invalid option! Defaulting to Classic Mode.")
            self.classic_mode()

    def classic_mode(self):
        self.lower = 1
        self.upper = 100

        print(Fore.GREEN + "\nYou have chosen Classic Mode!")
        print(Fore.GREEN + f"Guess the number between {self.lower} and {self.upper}.")

        self.x = random.randint(self.lower, self.upper)

        self.total_chances = math.ceil(math.log(self.upper - self.lower + 1, 2))
        print(Fore.GREEN + f"You have {self.total_chances} chances to guess the number!\n")

        self.play_game()

    def time_challenge_mode(self):
        self.lower = 1
        self.upper = 100

        print(Fore.GREEN + "\nYou have chosen Time Challenge Mode!")
        print(Fore.GREEN + f"Guess the number between {self.lower} and {self.upper}. You have 30 seconds!\n")

        self.x = random.randint(self.lower, self.upper)

        start_time = time.time()

        while True:
            guess = int(input(Fore.YELLOW + "Enter your guess: "))
            elapsed_time = time.time() - start_time

            if elapsed_time > 30:
                print(Fore.RED + "\nTime's up! You didn't guess the number in time.")
                print(Fore.RED + f"The number was {self.x}")
                break

            if guess == self.x:
                print(Fore.GREEN + f"Congratulations! You guessed correctly in {elapsed_time:.2f} seconds!")
                break
            elif guess < self.x:
                print(Fore.RED + "Too low! Try again.\n")
            else:
                print(Fore.RED + "Too high! Try again.\n")

    def infinite_mode(self):
        self.lower = 1
        self.upper = 100

        print(Fore.GREEN + "\nYou have chosen Infinite Mode!")
        print(Fore.GREEN + f"Guess the number between {self.lower} and {self.upper}. You can play indefinitely until you guess correctly or quit!\n")

        self.x = random.randint(self.lower, self.upper)
        attempts = 0

        while True:
            guess = int(input(Fore.YELLOW + "Enter your guess or type -1 to quit: "))

            if guess == -1:
                print(Fore.CYAN + "You chose to quit. Thank you for playing!")
                break

            attempts += 1

            if guess == self.x:
                print(Fore.GREEN + f"Congratulations! You guessed correctly after {attempts} attempts!")
                break
            elif guess < self.x:
                print(Fore.RED + "Too low! Try again.\n")
            else:
                print(Fore.RED + "Too high! Try again.\n")

    def play_game(self):
        self.count = 0
        self.flag = False

        while self.count < self.total_chances:
            self.count += 1

            guess = int(input(Fore.YELLOW + f"Attempt {self.count}: Enter your guess between {self.lower} and {self.upper}: "))

            if self.x == guess:
                print(Fore.GREEN + f"Congratulations! You guessed correctly in {self.count} attempts!")
                self.flag = True
                break
            elif guess < self.x:
                print(Fore.RED + "Too low! Try again.\n")
            elif guess > self.x:
                print(Fore.RED + "Too high! Try again.\n")

        if not self.flag:
            print(Fore.RED + f"\nThe number was {self.x}")
            print(Fore.CYAN + "Better luck next time!")


if __name__ == "__main__":
    game = NGuessBoardUI()