import tkinter as tk
from tkinter import messagebox
import random

class WordleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle")
        self.master.geometry("400x500")
        self.master.resizable(False, False)

        self.word_list = self.load_words("wordle_words.txt")
        self.secret_word = self.choose_word()
        self.attempts = 6
        self.current_row = 0

        self.create_widgets()

    def load_words(self, filename):
        with open(filename, 'r') as file:
            return [word.strip().upper() for word in file]

    def choose_word(self):
        return random.choice(self.word_list)

    def create_widgets(self):
        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(pady=20)

        self.grid = []
        for i in range(6):
            row = []
            for j in range(5):
                cell = tk.Label(self.grid_frame, width=4, height=2, relief="raised", font=("Arial", 20, "bold"))
                cell.grid(row=i, column=j, padx=2, pady=2)
                row.append(cell)
            self.grid.append(row)

        self.entry = tk.Entry(self.master, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

    def submit_guess(self):
        guess = self.entry.get().upper()
        if len(guess) != 5 or guess not in self.word_list:
            messagebox.showerror("Invalid Guess", "Please enter a valid 5-letter word.")
            return

        self.check_guess(guess)
        self.entry.delete(0, tk.END)

        if guess == self.secret_word:
            messagebox.showinfo("Congratulations!", f"You guessed the word {self.secret_word}!")
            self.master.quit()
        elif self.current_row == 5:
            messagebox.showinfo("Game Over", f"The word was {self.secret_word}.")
            self.master.quit()

        self.current_row += 1

    def check_guess(self, guess):
        for i, letter in enumerate(guess):
            cell = self.grid[self.current_row][i]
            cell.config(text=letter)

            if letter == self.secret_word[i]:
                cell.config(bg="green", fg="white")
            elif letter in self.secret_word:
                cell.config(bg="yellow", fg="black")
            else:
                cell.config(bg="gray", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    wordle_gui = WordleGUI(root)
    root.mainloop()