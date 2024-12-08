import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("600x400")  # Adjusted size
        self.master.resizable(False, False)

        # Variables
        self.target_number = 0
        self.attempts = 0
        self.max_attempts = None
        self.max_num = 100
        self.game_in_progress = False  # Flag to track if a game is ongoing

        # UI Elements
        self.label_title = tk.Label(master, text="Number Guessing Game", font=("Arial", 20))  # Larger font
        self.label_title.pack(pady=15)  # Adjusted padding

        self.label_instructions = tk.Label(master, text="Choose a difficulty level to start:", font=("Arial", 14))
        self.label_instructions.pack(pady=10)

        self.button_easy = tk.Button(master, text="Easy (1–10)", command=lambda: self.start_game(10, None), width=20)
        self.button_easy.pack(pady=5)

        self.button_medium = tk.Button(master, text="Medium (1–50)", command=lambda: self.start_game(50, 10), width=20)
        self.button_medium.pack(pady=5)

        self.button_hard = tk.Button(master, text="Hard (1–100)", command=lambda: self.start_game(100, 7), width=20)
        self.button_hard.pack(pady=5)

        self.label_feedback = tk.Label(master, text="", font=("Arial", 14))
        self.label_feedback.pack(pady=15)

        self.entry_guess = tk.Entry(master, font=("Arial", 14), state="disabled", width=15)
        self.entry_guess.pack(pady=5)

        self.button_submit = tk.Button(master, text="Submit Guess", command=self.check_guess, state="disabled", width=15)
        self.button_submit.pack(pady=5)

        # Exit button
        self.button_exit = tk.Button(master, text="Exit", command=self.exit_game, width=20)
        self.button_exit.pack(pady=15)

    def start_game(self, max_num, max_attempts):
        # Check if a game is already in progress
        if self.game_in_progress:
            messagebox.showwarning("Game in Progress", "Please finish the current game before starting a new one.")
            return  # Exit the method if a game is in progress

        # Initialize the new game
        self.max_num = max_num
        self.target_number = random.randint(1, max_num)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.game_in_progress = True  # Set the flag to indicate a game is in progress

        # Update UI for the new game
        self.label_feedback.config(text=f"Guess the number between 1 and {max_num}!")
        self.entry_guess.config(state="normal")
        self.button_submit.config(state="normal")

        # Notify the player
        messagebox.showinfo("Game Started", f"Game started! Range: 1–{max_num}. Max attempts: {max_attempts or 'Unlimited'}.")

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.entry_guess.delete(0, tk.END)

            if guess > self.max_num:
                messagebox.showerror("Out of Range", f"The number is within 1 and {self.max_num}. Try again.")
                return

            if guess < self.target_number:
                feedback = "Too low!"
            elif guess > self.target_number:
                feedback = "Too high!"
            else:
                feedback = f"Correct! The number was {self.target_number}. You guessed it in {self.attempts + 1} attempts."
                messagebox.showinfo("Congratulations", feedback)
                self.reset_game()
                return

            self.attempts += 1

            if self.max_attempts and self.attempts >= self.max_attempts:
                self.end_game()
            else:
                self.label_feedback.config(text=f"{feedback} Attempts: {self.attempts}/{self.max_attempts or '∞'}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def end_game(self):
        messagebox.showerror("Game Over", f"You've failed to guess the number! It was {self.target_number}.")
        self.reset_game()

    def reset_game(self):
        self.entry_guess.config(state="disabled")
        self.button_submit.config(state="disabled")
        self.label_feedback.config(text="Choose a difficulty level to start again.")
        self.game_in_progress = False  # Reset the flag after game ends

    def exit_game(self):
        # Close the application when the Exit button is clicked
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.quit()

# Create the GUI application
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()