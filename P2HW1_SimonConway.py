    #A Total price of all five items
    # 04/17/2022
    # CTI-110 P2HW1 - Total Purchases
    # Simon Conway
    # Collect input 1
    # Collect input 2
    # Collect input 3
    # Collect input 4
    # Collect input 5
    # Calculate subtotal by adding input togather
    # Calculate saletax by multipyling subtotal by seven percent
    # Calculate total price by adding saletax and subtotal
    # Display output for subtotal,saletax, and total
P1 = float(input('Enter price of item #1'))
P2 = float(input('Enter price of item #2'))
P3 = float(input('Enter price of item #3'))
P4 = float(input('Enter price of item #4'))
P5 = float(input('Enter price of item #5'))
subtotal = ( P1 + P2 + P3 + P4 + P5 )
sale_tax = (subtotal * 0.07)
total_price = ( sale_tax + subtotal)
print('Results')
print('subtotal:${:.2f}'.format(subtotal))
print('sale tax:${:.2f}'.format(sale_tax))
print('total price:${:.2f}'.format(total_price))
    
