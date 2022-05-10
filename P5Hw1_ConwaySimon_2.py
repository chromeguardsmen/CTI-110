# User created a function to collect the scoresof perivius grades.
# Placed in the correct number of scores ofr the program
# Created a function that evaluates the score that were place into it
# Function then does the evaluation is able to return the results it finds to the statement
# Return the statement and display
# Make sure each of the statements have a proper name
# 5/09/2022
# CTI-110 P5HW1 - Score List
# Simon Conway
#





n=int(input("How many scores you want to enter? "))

def collect_scores(n):

    lst=[]

    for i in range(1,n+1):

        valid_score=int(input(f"Enter Score #{i} "))

        if valid_score>=0 and valid_score<=100:

            lst.append(valid_score)

        else:

            while valid_score<0 or valid_score>100:

                print("Invalid Score Entered!!!")

                print("score Should be between 0 and 100")

                valid_score=int(input(f"Enter Score #{i} -again "))

    return lst

def evaluate(lst):

    print("Results")

    print("Lowest Score:",min(lst))

    lst.remove(min(lst))

    print("Modified List",lst)

    average=sum(lst)/len(lst)

    print("Scores Average",average)

    if average>=90 and average<=100:

        print("A")

    elif average>=80 and average<=89:

        print("B")

    elif average>=70 and average<=79:

        print("C")

    elif average>=60 and average<=69:

        print("D")

    else:

        print("E")

    print('Results')

lst=collect_scores(n)

evaluate(lst)



def collect_scores(n):
    lst=[]
    for i in range(1,n+1):
        valid_score=int(input(f"Enter Score #{i} "))
        if valid_score>=0 and valid_score<=100:
            lst.append(valid_score)
        else:
            while valid_score<0 or valid_score>100:
                print("Invalid Score Entered!!!")
                print("score Should be between 0 and 100")
                valid_score=int(input(f"Enter Score #{i} -again "))
    return lst
def evaluate(lst):
    print("Results")
    print("Lowest Score:",min(lst))
    lst.remove(min(lst))
    print("Modified List",lst)
    average=sum(lst)/len(lst)
    print("Scores Average",average)
    if average>=90 and average<=100:
        print("A")
    elif average>=80 and average<=89:
        print("B")
    elif average>=70 and average<=79:
        print("C")
    elif average>=60 and average<=69:
        print("D")
    else:
        print("E")
    print('Results')


while True:
    lst=None
    print("\n-MENU")  
    print("1) Create Score List")  
    print("2) Display Results")  
    print("3) Exit")  
    choice1 = int(input("Enter the Choice:"))  
  
    if choice1 == 1:
        n=int(input("How many scores you want to enter? "))
        lst=collect_scores(n)
        print("\n-MENU")  
        print("1) Create Score List")  
        print("2) Display Results")  
        print("3) Exit") 
        choice2 = int(input("Enter the Choice:"))  
  
        if choice2 == 1:  
            print("List already created")
              
        elif choice2 == 2:
            evaluate(lst)
            
              
        elif choice2 == 3:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 2:
        if lst==None:
            while lst==None:
                print("List not created yet")
                print("\n-MENU")  
                print("1) Create Score List")  
                print("2) Display Results")  
                print("3) Exit")
                choice3 = int(input("Enter the Choice:"))
        else:
            print("\n-MENU")  
            print("1) Create Score List")  
            print("2) Display Results")  
            print("3) Exit")
            choice3 = int(input("Enter the Choice:"))  
  
        if choice3 == 1:  
           print("list already created")
              
        elif choice3 == 2:  
            evaluate(lst)
              
        elif choice3 == 3:  
            break
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 3:  
        break  
      
    else:  
        print("Oops! Incorrect Choice.")  
