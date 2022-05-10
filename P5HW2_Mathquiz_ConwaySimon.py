# With the use of functions,modules and loops i have created a math quiz.
# With said quiz i have been able to make a math quiz that will operate using subtraction and addition
# 5/9/2022
# CTI-110 P5HW2 - Math Quiz
# Simon Conway
# Generate first random number between 1 and 1000
# Generate second number
# Display the question in a correct format
# Ask the user to enter their answer
# Check if the user answer is correct
# Generate first random number between 1 and 1000
# Generate second number
# Display the question in correct format
# Ask user to enter their answer
# Check if the user answer is correct
# Display the correct answer
# Run loop till user enters 3
# Display the menu
# Ask user to enter their choice
# Check if the user choice is 1
# Check if the user choice is 2
# Check if the user choice is 3
# Stop the program

import random

def additionQuiz():
    """
    Function to generate addition quiz
    Two numbers generated X and Y
    OUTPUT
      X
    + Y 
    ---
    Result by user
    """
    X = random.randint(1,1000) 
    Y = random.randint(1,1000) 

    print("  {}\n+ {}\n------".format(X,Y))
    
    userAnswer = int(input(" "))
    correctAnswer = X + Y

    if userAnswer == correctAnswer:
        print("Congratulations!")
    else:
        print("Wrong answer!")
        print("Correct answer is: {}".format(correctAnswer))


def subtractionQuiz():
    """
    Function to generate addition quiz
    Two numbers generated X and Y
    OUTPUT
      X
    - Y 
    -----
    Result by user
    """
    X = random.randint(1,1000) 
    Y = random.randint(1,1000) 

    
    print("  {}\n- {}\n------".format(X,Y))
    
    userAnswer = int(input("  "))
    correctAnswer = X - Y
    
    if userAnswer == correctAnswer:
        print("Congratulations!")
    else:
        print("Wrong answer!")
        
        print("Correct answer is: {}".format(correctAnswer))


runProgram = True
while runProgram:
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    
    userChoice = int(input("Enter your choice: "))
   
    if userChoice == 1:
        additionQuiz()
    
    elif userChoice == 2:
        subtractionQuiz()
    
    elif userChoice == 3:
        runProgram = False 
