import random

class hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 3
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input("Guess a Lletter please. ")
            if guess.isalpha() and len(guess) == 1:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                #Adds wrong and right guesses to variable list_of_guesses
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)

    def check_guess(self,guess):
        guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word. {self.word}")
            print(self.word_guessed)
        else:
            self.num_lives =-1
            print(f"Sorry, {guess} is not in the word. Try again. {self.word}")
            print(f"You have {self.num_lives} lives left.")
        for index,letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess

                print(guess)
                print(self.word_guessed)
        self.num_letters =-1

                #change word guessed in that position to whatever guess is

                #self.word_guessed = [i for i, letters in enumerate(self.word) if letters == guess]
                #.replace([self.word.index(i)])

                #print(self.word_guessed)
#        #of index I only. #append method not working, no imports needed trid indentation still not working in our out of class/functions
#     num_letters = +1
    

        

word_list = ["grapes", "oranges", "apples", "blueberries", "strawberries"]
game = hangman(word_list)
game.check_guess("a")

