#------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

#This loop is for displaying the questions and options.
    for key in questions:
        print("------------------------------")
        print(key)
        for i in option[question_num-1]:
            print(i)

#This is where user will input there answer.
        guess = input("Enter your answer(A, B, C or D)").upper()
        guesses.append(guess)

#This is where we are checking our answers.
        correct_guesses += check_answer(questions.get(key), guess)
        question_num +=1

#This is where we are showing the result.
    display_score(correct_guesses, guesses)

#------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("RESULTS")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

#This is where we are calculating our score.
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#------------------------------
def play_again():
    response = input("Do you want to play again?(Yes/No): ").upper()
    if response == "YES":
        return True
    else:
        return False
#------------------------------

questions = {
    "Who created Pyhton?": "A",
    "What year python was created?": "B",
    "Python is tributed to which comedy group?": "C",
    "Is earth round? ": "A"
}

option = [["A. Guido Van Rossum","B. Elon Musk","C. Bill Gates","D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991","C. 2000","D. 2016"],
          ["A. Lonely Island","B. Smosh","C. Monty Python","D. SNL"],
          ["A. True","B. False","C. Sometimes","D. What's Earth"]
          ]
new_game()

while play_again():
    new_game()

print("Bye!!!!")