import random
import math
import time
import tkinter as tk
from tkinter import messagebox

class NGuessBoardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.root.geometry("500x500")
        self.root.configure(bg="#333333")

        self.x = 0
        self.lower = 1
        self.upper = 100
        self.total_chances = 0
        self.count = 0
        self.start_time = 0
        self.mode = tk.StringVar(value="Classic")
        self.game_running = False

        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(self.root, text="Welcome to the Number Guessing Game!", font=("Arial", 18, "bold"), fg="#FFD700", bg="#333333")
        title_label.pack(pady=15)

        instruction_label = tk.Label(self.root, text="Select the game mode and guess the number!", font=("Arial", 12), fg="#FFFFFF", bg="#333333")
        instruction_label.pack(pady=5)

        mode_label = tk.Label(self.root, text="Choose Game Mode:", font=("Arial", 14, "italic"), fg="#FFFFFF", bg="#333333")
        mode_label.pack(pady=5)

        mode_menu = tk.OptionMenu(self.root, self.mode, "Classic", "Time Trial", "Infinite")
        mode_menu.config(font=("Arial", 12), bg="#4CAF50", fg="white", relief=tk.GROOVE)
        mode_menu.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Game", font=("Arial", 12, "bold"), command=self.start_game, bg="#FFA500", fg="white", relief=tk.RAISED, bd=5)
        self.start_button.pack(pady=15)

        guess_label = tk.Label(self.root, text="Enter your guess:", font=("Arial", 12), fg="#FFFFFF", bg="#333333")
        guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.root, font=("Arial", 14), justify='center', relief=tk.SUNKEN, bd=4)
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit Guess", font=("Arial", 12, "bold"), command=self.check_guess, state=tk.DISABLED, bg="#2196F3", fg="white", relief=tk.RAISED, bd=5)
        self.submit_button.pack(pady=15)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), fg="#FFD700", bg="#333333")
        self.feedback_label.pack(pady=10)

    def start_game(self):
        mode = self.mode.get()
        self.game_running = True
        self.count = 0

        if mode == "Classic":
            self.lower, self.upper = 1, 100
            self.x = random.randint(self.lower, self.upper)
            self.total_chances = math.ceil(math.log(self.upper - self.lower + 1, 2))
            self.feedback_label.config(text=f"Classic Mode: You have {self.total_chances} chances.")

        elif mode == "Time Trial":
            self.lower, self.upper = 1, 100
            self.x = random.randint(self.lower, self.upper)
            self.start_time = time.time()
            self.feedback_label.config(text="Time Trial Mode: You have 30 seconds to guess!")

        elif mode == "Infinite":
            self.lower, self.upper = 1, 100
            self.x = random.randint(self.lower, self.upper)
            self.feedback_label.config(text="Infinite Mode: Keep guessing until you find the number!")

        self.submit_button.config(state=tk.NORMAL)

    def check_guess(self):
        if not self.game_running:
            return

        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")
            return

        self.count += 1
        mode = self.mode.get()

        if mode == "Classic":
            if guess == self.x:
                self.feedback_label.config(text=f"Congratulations! You guessed it in {self.count} attempts!")
                self.end_game()
            elif self.count >= self.total_chances:
                self.feedback_label.config(text=f"You lost! The number was {self.x}.")
                self.end_game()
            elif guess < self.x:
                self.feedback_label.config(text="Too low! Try again.")
            else:
                self.feedback_label.config(text="Too high! Try again.")

        elif mode == "Time Trial":
            elapsed_time = time.time() - self.start_time
            if elapsed_time > 30:
                self.feedback_label.config(text=f"Time's up! The number was {self.x}.")
                self.end_game()
            elif guess == self.x:
                self.feedback_label.config(text=f"Congratulations! You guessed it in {elapsed_time:.2f} seconds!")
                self.end_game()
            elif guess < self.x:
                self.feedback_label.config(text="Too low! Try again.")
            else:
                self.feedback_label.config(text="Too high! Try again.")

        elif mode == "Infinite":
            if guess == self.x:
                self.feedback_label.config(text=f"Congratulations! You guessed it after {self.count} attempts!")
                self.end_game()
            elif guess < self.x:
                self.feedback_label.config(text="Too low! Try again.")
            else:
                self.feedback_label.config(text="Too high! Try again.")

    def end_game(self):
        self.game_running = False
        self.submit_button.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", "Thank you for playing! You can start a new game anytime.")

root = tk.Tk()
app = NGuessBoardGUI(root)
root.mainloop()
