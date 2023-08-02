import random

word_list = ["grapes", "oranges", "apples", "blueberries", "strawberries"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word. {word}")
    else:
        print(f"Sorry, {guess} is not in the word. Try again. {word}")

def ask_for_input():
    while True:
        guess = input("Guess a letter please. ")
        if guess.isalpha() and len(guess) == 1:
            check_guess(guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()