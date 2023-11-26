'''
Guess the word with lives. from the words list, computer will choose a word randomly and user have to guess the letter of word. when user guess
all the letters in the word, game will be finished.
every time user guess a letter, it will be added to a list and random word will be shown to the user. user can see guessed letters only, other 
letters will have '_' or '-'.
added functionality is you have lives time lives to complete the task.
'''

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words).upper() # randomly choose a word from words
    while '-' in word or ' ' in word: # word should not contains hyphens ('-') or spaces (' ') 
        word = random.choice(words) 

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # user guessed letters
    lives = 10      # you have 10 lives to guess the full word

    while len(word_letters) > 0 and lives > 0:
        # show the letter used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have used these letters: ", ' '.join(used_letters))

        # what current word is (ie W - R K)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # remain lives
        print(f"You have only {lives} lives!!")

        # main logic
        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters: 
            used_letters.add(user_input) # add to user_letters when user_input is in alphabet but not in used_letters
            if user_input in word_letters:
                word_letters.remove(user_input) # remove from user_letters when user_input is in word_letters
            else:
                lives -= 1 # loss a live
        elif user_input in used_letters:
            print("You already have used that character. try again! ")
        else:
            print("Invalid character. Try again! ")
    
    # come here if word_letters == 0 or lives == 0
    if lives == 0:
        print("You lost!!")
    else:
        print(f"You have successfully guess the word {word}")

hangman()