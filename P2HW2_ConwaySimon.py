# CTI-110
# P2HW2 - Score Avg
# Simon Conway 
# 04/17/2022
# Collect input 1 - 7
# Determine the lowest score and store in a variable
# Drop lowest score from list
# Calculate Score average after having dropped lowest score
# Display Lowest score entered
# Display score List after dropping lowest score
# Display the average of scores in modified list
list = []
for i in range(7):
    list.append(float(input('Enter score #{}: '.format(i+1) )))
lowest_value = min(list)
list.sort()
without_min = list[1:-1]
average = sum(without_min)/6 
print(lowest_value)
print(without_min)
print(average)

