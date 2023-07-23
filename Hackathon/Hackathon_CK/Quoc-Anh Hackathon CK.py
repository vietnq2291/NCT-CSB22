# Bài 1 
num1 = int(input('Input the first number: '))
num2 = int(input('Input the second numer: '))
print (num1, '+',num2, '=', num1 + num2)

# Bài 2
from math import *
a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))
delta = b**2 - 4 * a * c 
x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b - sqrt(delta)) / 2 * a 
if delta < 0:
    print ('The equation has no solution.')
else: 
 if x1 == x2: 
    print ("The equation has 1 solution.")
    print (f'x = {x1}')
 elif x1 != x2:
    print ("The equation has 2 solutions.")
    print (f'x = {x1} or x = {x2}')

# Bài 3

def is_palindrome (n):
    reversed_text = ''
    for char in n:
        reversed_text = reversed_text + char
        if reversed_text == n:
            return (n)
User_input = input ('Input a text: ')
if is_palindrome(User_input):
    print ('This is a palindrome')
else: 
    print ('This is not a palindrome')

# Bài 4

print ('Welcome to MindX restaurant!')
menu = []
while True:
 customer_order = input ("Please choose a dish: ")
 if customer_order not in menu: 
     menu.append (customer_order)
     option = input ('Great choice! Anything else? (y/n): ')
 elif customer_order in menu:
     option = input ('You chose this already! Anything else? (y/n): ')
 if option == 'y':
     customer_order = input ("Please choose a dish: ")
     if customer_order not in menu: 
      menu.append (customer_order)
      option = input ('Great choice! Anything else? (y/n): ')
     elif customer_order in menu:
      option2 = input ('You chose this already! Anything else? (y/n): ')
      continue
 elif option == 'n' :
     print ('Well done! Your order: ')
     for food in range(len(menu)):
         print (f'- {menu[food]}')
     break

# Bài 5

Phone_price = {
    'Iphone12' : 28000000,
    'Samsung N10' : 16000000,
    'Oppo 93' : 7500000,
    'Vsmart' : 7400000,
    'Vivo' : 4200000  
}

find_price = input ("Input name of a phone: ")
if find_price not in Phone_price:
    print ('Phone not found.')
    find_price = input ("Input name of a phone: ")
if find_price in Phone_price:
    print ("Price of", find_price,':',Phone_price[find_price])

customer_budget = int (input('Input your budget: '))
print ("Phones that fit your budget: ")
fit_budget = []
for i in Phone_price:
    if Phone_price[i] <= customer_budget:
        fit_budget.append (i)
for x in fit_budget:
    print (f'- {x}')

# Bài 6

num_input = int (input("Input an integer: "))
str_num = str(num_input)
if num_input <= 0:
    print ("Please input an integer > 0.")
    num_input = int ("Input an integer: ")
else: 
    count = 0
    for digits in str_num:
        count += 1
    print (f" This number has {count} digits.")

# Bài 7
num_list = [5,1,8,92,-1,30]
print ("Original list: ",num_list)

l = len (num_list)
for i in range (0,l-1):
        for j in range (i+1,l):
            if num_list [i] > num_list [j]:
                x = num_list[i]
                num_list [i] = num_list [j]
                num_list [j] = x
    

print ("Sorted list: ",num_list)

# Bài 8 

user_Input2 = int (input("Input a number: "))
if user_Input2 <=1:
    print ("Please input a number >=2 ")
else: 
 Fibo_arr = [1,1]
 new_number = 0
 
 for num in range (2,user_Input2): 
    new_number = Fibo_arr [num-1] + Fibo_arr [num - 2]
    Fibo_arr.append (new_number)
    
print (f'First {user_Input2} Fibonacci numbers: {Fibo_arr}')
    
 
    
        
        
    
     

            
            
    
    