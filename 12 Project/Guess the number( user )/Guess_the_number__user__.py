import random
import time

def guessNumber():
    x = 1       #start
    y = 10      #end

    while True:
        if x != y:
            guessNumber = random.randint(x, y)      #will do when start != end
        else:
            guessNumber = random.randint(x, y)
        high = 'h'
        low = 'l'
        correct = 'c'
        userInput = input(f"Guess Number {guessNumber} High (h), Low (l), Correct (c) : ", ).lower()
        if userInput != "":
            if userInput == high:
                y = guessNumber - 1
            elif userInput == low:
                x = guessNumber + 1
            else:
                print("Correct")
                break
        else:
            print("Input must not be empty")

print("Note a number between 1 to 10")
time.sleep(3)       #just a 3 second timeout to think
guessNumber()

'''
Shorten Version
import random

def guessNumber():
    x, y = 0, 10

    while True:
        guessNumber = random.randint(x, y)
        userInput = input(f"Guess Number {guessNumber} High (h), Low (l), Correct (c) : ").lower()
        if userInput == 'h':
            y = guessNumber - 1
        elif userInput == 'l':
            x = guessNumber + 1
        else:
            print("Correct")
            break

guessNumber()

'''