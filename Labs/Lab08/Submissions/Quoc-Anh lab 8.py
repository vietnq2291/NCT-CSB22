#BT1
def is_int():
    return num.is_integer
num = float(input("Input a number: "))
if is_int(num):
    print (f'{int(num)} is an integer')
else: 
    print (f'{num} is not an integer')

#BT2
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range (2,n):
        if n % i == 1:
            return False

a = int(input("Input number: "))
if is_prime(a):
    print (a, "is a prime number") 
else:
    print (a, "is not a prime number")     

#BT3
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range (2,n):
        if n % i == 1:
            return False

num1 = int (input("Input a number: "))
prime_lis = []
lim = 0
for i in range (0,100000000000):
    if is_prime(i):
        prime_lis.append(i)
        lim += 1
    if lim == num1:
        break
    
print (f'First {num1} prime number(s): {prime_lis}')

#BT4

def factorial (x):
    factor = 1
    for i in range (1,x):
        factor = factor * i
    return factor 
def special_formula (x):
    special = 0
    for y in range (1,x):
        special = special + factorial(y)/y
    return special 
Inp_num = int(input("Input a number: "))
print ("Result: ",Inp_num)

#BT5
from datetime import *
day = date(2021,7,21)
hour = time (13,36,10)
print ('Today is: ',day.strftime ('%d/%m/%Y'))
print (f'Time right now: {hour}')


        
     
    
    
    
        
    
    
    
