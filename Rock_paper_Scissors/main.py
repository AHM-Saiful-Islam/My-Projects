import random

def play():
    user = input("what is your choice? 'r' for Rock, 'p' for Paper and 's' for Scissors:\n")
    computer = random.choice(['r', 'p', 's']) # computer will choose randomly rock or, paper or, scissors
    
    if user == computer:
        print("It's a tie!")   # for same choice

    elif is_win(user, computer):    # if user win then iswin() function will return true, hence 'if' condition get true value and return that you win!
        print("You won!")

    else:
        print("You lost!")

def is_win(player, opponent):
    # return true if player wins
    # rules: r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()