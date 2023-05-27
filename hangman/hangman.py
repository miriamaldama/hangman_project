#

import random
import os
import time

# Define play again:
def play_again():
    play_game = input("Do you want to play again? ")
    while play_game not in ["yes", "no", "Yes", "No"]:
        play_game = input("Sorry, didn't understand. Do you want to play again? ").lower()  
    if play_game.lower() == "yes":
        return True
    else:
        return False

# Define to play
def hangman(word):
    display = "_" * len(word)
    count = 0
    limit = 6
    letters = list(word)
    guessed = []
    incorrect_guesses = list()
    while count < limit:
        guess = input(f"Please enter a letter. Hangman word: {display}\n")
        while len(guess) == 0 or len(guess) > 1:
            print("Invalid input, enter a single letter\n")
            guess = input(
              f"Hangman Word: {display} Enter your guess: \n").strip() #The sintax f"{}""
            # is used to prompt the user while also displaying the underscores that will
            # vary acording to the different possible words to guess.
        if guess in letters:
             print("Yes, that's a correct one!")
             letters.remove(guess) # Method .remove() is used here to remove the first
             # occurence of a specified element from a list
             positions = []
             for i in range(len(word)):
                 if word[i] == guess:
                     positions.append(i)
             for pos in positions: 
                 display = display[:pos] + guess + display[pos + 1:] #to display as a string and not as a list
             print(display)
             if display == word:
                 print("You won! Congrats")
                 print("The word you guessed was:", word)
                 count = limit
                 break
             continue
        if guess in guessed:
            print("You already tried that one")
            print("So far guessed:", display)
            continue
        else:
            count = count + 1           
            if count == 1:
                 time.sleep(1) #Delays program execution for a sec.
                 print("Oops, that's not a correct guess")
                 incorrect_guesses.append(guess)
                 print("You have", 6 - count, "guesses left")
                 print('   _____ \n'
                       '  |     |\n'
                       '  |      \n'
                       '  |      \n'
                       '  |      \n'
                       '  |      \n'
                       '  |      \n'
                       '__|__\n')
                 incorrect_guesses_string = ', '.join(incorrect_guesses)
                 print("Incorrect guesses so far: " + incorrect_guesses_string)
                 print(display)
            if count == 2:
                 time.sleep(1) 
                 print("Oops, that's not a correct guess")
                 incorrect_guesses.append(guess)
                 print("You have", 6 - count, "guesses left")
                 print('   _____ \n'
                       '  |     |\n'
                       '  |     | \n'
                       '  |      \n'
                       '  |      \n'
                       '  |      \n'
                       '  |      \n'
                       '__|__\n')
                 incorrect_guesses_string = ', '.join(incorrect_guesses)
                 print("Incorrect guesses so far: " + incorrect_guesses_string)
                 print(display)
            if count == 3:
                 time.sleep(1) 
                 print("Oops, that's not a correct guess")
                 incorrect_guesses.append(guess)
                 print("You have", 6 - count, "guesses left")
                 print('   _____ \n'
                       '  |     |\n'
                       '  |     | \n'
                       '  |     o \n'
                       '  |       \n'
                       '  |      \n'
                       '  |      \n'
                       '__|__\n')
                 incorrect_guesses_string = ', '.join(incorrect_guesses)
                 print("Incorrect guesses so far: " + incorrect_guesses_string)
                 print(display)
            if count == 4:
                 time.sleep(1) 
                 print("Oops, that's not a correct guess")
                 incorrect_guesses.append(guess)
                 print("You have", 6 - count, "guesses left")
                 print('   _____ \n'
                       '  |     |\n'
                       '  |     | \n'
                       '  |     o \n'
                       '  |     | \n'
                       '  |      \n'
                       '  |      \n'
                       '__|__\n')
                 incorrect_guesses_string = ', '.join(incorrect_guesses)
                 print("Incorrect guesses so far: " + incorrect_guesses_string)
                 print(display)
            if count == 5:
                 time.sleep(1) 
                 print("Oops, that's not a correct guess")
                 incorrect_guesses.append(guess)
                 print("You have", 6 - count, "guess left")                
                 print('   _____ \n'
                       '  |     |\n'
                       '  |     | \n'
                       '  |     o \n'
                       '  |    /|\ \n'
                       '  |      \n'
                       '  |      \n'
                       '__|__\n')
                 incorrect_guesses_string = ', '.join(incorrect_guesses)
                 print("Incorrect guesses so far: " + incorrect_guesses_string)
                 print("Last Chance!")
                 print(display)
            if count == 6:
                 time.sleep(1) 
                 print("Oops, that was last chance")
                 incorrect_guesses.append(guess)
                 print("You have", 6 - count, "guesses left")
                 print('   _____ \n'
                       '  |     |\n'
                       '  |     | \n'
                       '  |     o \n'
                       '  |    --- \n'
                       '  |    /|\ \n'
                       '  |    / \ \n'
                       '__|__\n')
                 incorrect_guesses_string = ', '.join(incorrect_guesses)
                 print("Incorrect guesses: " + incorrect_guesses_string)
                 print("You've been hanged!")
                 print("We were looking for:", word)
         
# Start playing

def play_hangman():
    print("Hi! Welcome to the Hangman Game")
    print("   \o/  \n"
          "    |   \n"
          "   / \   \n")
    name = input("Enter your name: ")
    print(f"Hello {name}! Best of luck!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    lst = open("hangman_words.txt")
    posible_words = list()
    for line in lst:
        line = line.rstrip()
        posible_words.append(line)

    play = True
    while play:
        word = random.choice(posible_words)
        hangman(word)
        play = play_again()
    print("Thanks for Playing! Bye!")
    print("   \o/  \n"
          "    |   \n"
          "   / \   \n")
    exit()

if __name__ == '__main__':
  play_hangman()

