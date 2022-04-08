#'This project is being design for find the number of pizzas that each student will recevie if each pizza has three slices,so one pizzza for every two students 
#'4/8/2022
#'CTI-110P1HW2-Pizza-Order
#'Simon-Conway
numstudents = int(input('How many stuednts do you want to order pizza for?'))
numslices = numstudents*3
numpizzasshared = numslices/6
print('Pizza Order')
print('Number of Students',numstudents)
print('Pizza Slices Needed',numslices)
print('Pizzas Needed',numpizzasshared)

