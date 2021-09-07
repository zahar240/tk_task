"""You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more than one, they get a 10% discount on all of them!
Given the total number of kaleidoscopes that a customer buys, let them know what their total will be. 
Tax is 7%. All of your kaleidoscopes cost the same amount, 5.00.

Task: 
Take the number of kaleidoscopes that a customer buys and output their total cost including tax and any discounts.

Input Format: 
An integer value that represents the number of kaleidoscopes that a customer orders.

Output Format: 
A number that represents the total purchase price to two decimal places.

Sample Input: 
4

Sample Output: 
19.26"""

def sale_kaleidoscopes(count):
    if count > 1:
        sale = count * 5 * 0.9 * 1.07
    elif count == 1:
        sale = 5.35
    return round(sale, 2)

count_kaleidoscopes = int(input("Введите целое число: "))

print(sale_kaleidoscopes(count_kaleidoscopes))