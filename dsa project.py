import tkinter as tk
from tkinter import messagebox
import random

class Node:
    def __init__(self, char):
        self.char = char
        self.next = None

class WordLinkedList:
    def __init__(self, word):
        self.head = None
        for char in word:
            self.add_char(char)

    def add_char(self, char):
        if not self.head:
            self.head = Node(char)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(char)

    def display_word(self, guesses):
        display = ''
        current = self.head
        while current:
            if current.char in guesses:
                display += current.char + ' '
            elif current.char == ' ':
                display += '  '
            else:
                display += '_ '
            current = current.next
        return display

class WordGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guessing Game")

        self.words = ['algorithm', 'programming', 'binary', 'compiler',
                      'data', 'structure', 'variable', 'loop',
                      'function', 'class', 'object', 'pointer']

        self.word = random.choice(self.words)
        self.word_linked_list = WordLinkedList(self.word)

        self.guesses = ''
        self.turns = 7

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, text="Guess the characters:", font=("Arial", 14))
        self.word_label.grid(row=0, column=0, columnspan=2)

        self.display_word_label = tk.Label(self.master, text=self.word_linked_list.display_word(self.guesses), font=("Arial", 16))
        self.display_word_label.grid(row=1, column=0, columnspan=2)

        self.guess_label = tk.Label(self.master, text="Enter a letter:", font=("Arial", 14))
        self.guess_label.grid(row=2, column=0)

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_guess, font=("Arial", 14))
        self.submit_button.grid(row=3, column=0, columnspan=2)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy, font=("Arial", 14))
        self.quit_button.grid(row=4, column=0, columnspan=2)

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Invalid input! Please enter a single letter.")
            return

        if guess in self.guesses:
            messagebox.showinfo("Information", "You already guessed that letter!")
            return

        self.guesses += guess

        if guess not in self.word:
            self.turns -= 1
            if self.turns == 0:
                messagebox.showinfo("Game Over", "You Lose! The word was: " + self.word)
                self.master.destroy()
            else:
                messagebox.showinfo("Incorrect Guess", f"Wrong! You have {self.turns} more guesses.")
        else:
            if set(self.word).issubset(set(self.guesses)):
                messagebox.showinfo("Congratulations", "You Win! The word was: " + self.word)
                self.master.destroy()

        self.display_word_label.config(text=self.word_linked_list.display_word(self.guesses))

def main():
    root = tk.Tk()
    game = WordGuessingGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
