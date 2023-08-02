import random

word_list = ["grapes" ,"oranges", "apples", "blueberries","strawberries"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter.....")
print(guess)

if len(guess) == 1:
    print("Good guess!")
else: 
    print("Oops! That is not a valid input.")