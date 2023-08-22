import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def ask_for_input(self):
        while self.num_lives > 0 and '_' in self.word_guessed:
            guess = input("Guess a letter please: ").lower()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
            else:
                print("Please enter a single alphabetical character.")

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
                    print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def play(self):
        self.ask_for_input()
        if '_' in self.word_guessed:
            print(f"Sorry, you're out of lives. The word was '{self.word}'.")
        else:
            print(f"Congratulations! You've guessed the word: {''.join(self.word_guessed)}")

word_list = ["grapes", "oranges", "apples", "blueberries", "strawberries"]
game = Hangman(word_list)
game.play()

