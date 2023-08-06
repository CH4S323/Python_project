import random
import string

#word to guess
#word_list = ("shit", "fuck", "dog")
word_list = ("fffffff", "gggggg")
word2Guess = random.choice(word_list).upper()
letterInWord = list(word2Guess)



#to check 
AtoZ = set(string.ascii_uppercase)

#guess character
usedLetter = set()

#lived count
count = 6
dash = '-'
#checking input is valid or not
while len(letterInWord) > 0 and count > 0:

    #to show already guess character 
    print("Used Character : ", " ".join(usedLetter ))

    #to show Correct Guess
    correctGuess = [c if c in usedLetter else '-' for c in word2Guess]
    print("Correct Guess : ", " ".join(correctGuess))

    #to break loop when guessed it
    if dash not in correctGuess:
        break

    #to show player lives
    print(f"You still have {count} lives")

    #user input 
    userInput = input("Guess a character : ").upper()


    if userInput in AtoZ - usedLetter:
        usedLetter.add(userInput)
        if userInput in letterInWord:
            letterInWord.remove(userInput)
    else:
        print("U just guess that character \n")

    count -= 1
if count == 0:
    print("You lose")
else:
    print("You guessed it")

