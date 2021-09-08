"""You and three friends go to a baseball game and you offer to go to the concession stand for everyone. 
They each order one thing, and you do as well. Nachos and Pizza both cost $6.00. 
A Cheeseburger meal costs $10. Water is $4.00 and Coke is $5.00. Tax is 7%.

Task 
Determine the total cost of ordering four items from the concession stand. 
If one of your friend’s orders something that isn't on the menu, you will order a Coke for them instead.

Input Format
You are given a string of the four items that you've been asked to order that are separated by spaces.

Output Format 
You will output a number of the total cost of the food and drinks.

Sample Input 
'Pizza Cheeseburger Water Popcorn'

Sample Output 
26.75"""

def total_check(order):
    order_price = {
        "nacho" : 6,
        "pizza" : 6, 
        "cheeseburger" : 10, 
        "water" : 4, 
        "coke" : 5
    }
    tax = 7
    total_result = 0
    for position in order:
        if position in order_price:
            total_result += order_price[position]
        elif position not in order_price:
            total_result += order_price["coke"]
    total_result_tax = total_result * (100 + tax) / 100
    return round(total_result_tax, 2)
    
ballpark_order = input("Введите список из четырех покупок через пробел: ").lower().split()

print(total_check(ballpark_order))


    