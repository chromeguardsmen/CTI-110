# Placeing in numerical grades in foor letter grade results
# My last name- Conway

def main():

    #This program takes a number grade and outputs a letter grade
    # System uses 10-point grading scale
    A_score = 90
    # To Do: Define  the rest of the score
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    #read the score from user
    #int() is used to convert number entered in string formal to integer
    score=int(input('Please Enter Score:'))
    #check the score belongs to which grade
    #91-100 grade is A
    #score>90 means 91-100
    if score>A_score:


            print('Your grade is: A')


    else:

        #score>=80
        if score>= B_score:


        #displaygrade
            print('Your grade is : B')



        else:

        #score>=70
            if score>=C_score:

        #displaygrade
                print('Your grade is: C')

            else:

        #score>=60
                if score>=D_score:

        #displaygrade
                    print('Your grade is: D')

                else:

        #score>=50
                    if score>=F_score:

        #displaygrade
                        print('Your grade is: F')

#programstart
#call the main function
main()


    
        
