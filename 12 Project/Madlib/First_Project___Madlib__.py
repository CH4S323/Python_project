


print("Madlib Program")

question_string = "What the ____ do u mean"
print(question_string)


answer_list = {
    1 : "fuck",
    2 : "shit",
    3 : "heck"
    }
#To show answer
def showAnswer():
    print("Choose a number from following answers")
    for key, value in answer_list.items():
        print(f"{key} : {value}")

showAnswer()

#Correct Answer
answer_key = 2
answer_value = "shit"

while True:
    try:
        testInput = input()
        if testInput.isdigit():     #checking digit or not
            testInput = int(testInput)

            if testInput not in range(1, len(answer_list) + 1):     #checking input in the list or not
                raise ValueError("Answer not in range")

            if testInput != answer_key:     #checking correct answer
                raise ValueError("Wrong answer")

            question_string = f"What the {answer_list[testInput]} do u mean"
            print("Answer : " + question_string)        
        else:
            if testInput == " ":        #checking input is empty or not
                raise ValueError("Answer must not be empty")
            for key, value in answer_list.items():
                if value != testInput:      #checking input is in list or not
                    raise ValueError("Answer not in the list")
                else:
                    if value != answer_value:       #checking correct answer
                        raise ValueError("Wrong Answer")
                question_string = f"What the {answer_list[key]} do u mean"
                print("Answer : " + question_string)
        break
    except ValueError as e:
        print(e)
        showAnswer()







    






