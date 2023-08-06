import random

print("Second project")

def guessGame():
    randomNumber = random.randint(1,10)

    while True:
        userInput = int(input("Guess the number between 1 to 10 : "))
        if userInput > randomNumber:
            print("too high")
        elif userInput < randomNumber:
            print("too low")
        else:
            print("You guess it right")
            break

guessGame()


