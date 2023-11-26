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



'''
Guessing Game with Computer
Computer will guess the number and we will give feedback.
'''
def computer_guess(y):
     low_limit = 1 # lower limit of guess
     high_limit = y # higher limit of guess
     feedback = "" # out feedback - could be c or h or l

     while feedback != "c":
          if low_limit != high_limit:
              guess_by_computer = random.randint(low_limit, high_limit)
          else:
               guess_by_computer = low_limit # It could be high_limit also, as low_limit = high_limit
               break # when two limits are same then there is no need to proceed further
          
          feedback = input(f"Is {guess_by_computer} too high (H), too low (L), or correct (C): ").lower() 

          if feedback == "h":
               high_limit = guess_by_computer - 1 # reset the limit
          elif feedback == "l":
               low_limit = guess_by_computer + 1 # reset the limit
     
     print(f"Congrats Computer! you have successfully guessed the number {guess_by_computer}.")

computer_guess(100)