# 100 days of Python
# Day 07 - Hangman

#Step 1 

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random
from day07_var import *
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Step 2

# Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for letter in chosen_word:
  display.append("_")

#Step 3

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#Step 4

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

won = False

#Step 5

# Update the word list to use the 'word_list' from hangman_words.py
# Import the logo from hangman_art.py and print it at the start of the game.

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

while not won:
  guess = input("\nGuess a letter: ").lower()

  # If guess is not a letter in the chosen_word,
  #Then reduce 'lives' by 1. 
  #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    print(guess + " is not in the word. You lose a life.")

  if lives == 0:
    print("Game over")
    print(stages[lives])
    break

  # If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print("You already guessed " + guess)
  
  for i in range(word_length):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = letter

  print(f"{' '.join(display)}")

  if "_" not in display:
    won = True
    print("You win!")

  # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

  print(stages[lives])
