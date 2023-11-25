'''
Guessing Game: 
Guess a number 
'''
import random

def guess(x):
     randon_number = random.randint(1, x)
     guess = 0
     while guess != randon_number:
          guess = int(input(f"Guess a number from 1 to {x}: "))
          if guess > randon_number:
               print("Oh no! you have to guess a smaller number")
          elif guess < randon_number:
               print("Wrong answer! you have to choose a bigger number")
     print("Congrats! you have done it.")

guess(10)