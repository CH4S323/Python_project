import random



print("Rock Paper Scissor")
userInput = input("Choose Rock (R), Paper (P), Scissor (S) : ", ).lower()
gameList = ('r', 'p', 's')
computer = random.choice(gameList)


while userInput not in gameList:
    print("Enter valid input")
    userInput = input("Choose Rock (R), Paper (P), Scissor (S) : ", ).lower()

if userInput == 's':
    if computer == 'p':
        print("You win")
    elif computer == 'r':
        print("You lose")
    else:
        print("Tie")
elif userInput == 'r':
    if computer == 'p':
        print("You lose")
    elif computer == 'r':
        print("Tie")
    else:
        print("You win")
else:
    if computer == 'p':
        print("Tie")
    elif computer == 'r':
        print("You win")
    else:
        print("You lose")

    print("Enter valid input")


''' 
Shorten version

if userInput == computer:
    print("Tie")
elif (userInput == 'r' and computer == 's') or (userInput == 's' and computer == 'p') or (userInput == 'p' and computer == 'r'):
    print("You win")
else:
    print("You lose")

'''




