#CTI-110
#P3HW2 - Pizza Order
#Simon Conway
#04/28/2022
#Answers user to enter number of students she/he would like to order pizza for.
#Ask user for number of people that will be sharing each pizza
#Accept user input for number of students
#Accept user input for number of people per pizza
#If people per pizza is valid then calculate the number of pizza and price
numstudents = int(input('How many students do you want to order pizza for?'))
numpeople = float(input('Enter the number of people per pizza(1.5,2 or 3):'))
print('Pizza order')

print('Number of students',numstudents)

print('Error:Please enter 1.5,2,or 3 ')

print('Please run program again')

if (numpeople == 1.5 or numpeople == 2 or numpeople == 3):

 whole_pizza=(numstudents/numpeople)

 price = whole_pizza * 5

 price = price + (price*0.06)

 print('Number of whole pizza',whole_pizza)

 print("Price:$",price)

 #had a large amount of trobule with assignment and had to get help with it mostly due to the if statement



