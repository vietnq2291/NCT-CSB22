from datetime import datetime 

#BT1: 
num = float(input("Input number: "))
def is_int(num):
    if num % 1 == 0:
        return True
    else:
        return False
    
if is_int(num):
    print(f"{int(num)} is an integer.")
else: 
    print(f"{num} is not an integer.")



#BT2: 
num2 = int(input("Input number: "))
def is_prime(num2):
    if num2 < 2:
        return False
    if num2 == 2:
        return True
    for x in range(2, int(num2/2)+1):
        if num2 % x == 0:
            return False
    return True
        
if is_prime(num2):
    print(f"{num2} is a prime number.")
else:
    print(f"{num2} is not a prime number.")

#BT3: 
def prime_list(num3):
    count = 0
    base = 2
    while count < num3: 
        for x in range(num3):
            if is_prime(base) == True:
                print(base, end=" ")
                count += 1
            base += 1
 
num3 = int(input("Input number: "))
prime_list(num3)

#BT4: 
def calc(num4):
    res = 0
    base = 1
    for x in range(1, num4+1):
         base *= x 
    res = (base/num4)
    print(int(res))
    base = 0
    res = 0
num4 = int(input("Input number: "))         
calc(num4)         

#BT5: 
def formulateDt():
    now = datetime.now()
    print(f"\nToday is {now.strftime('%d/%m/%Y')}.", f"\nTime right now: {now.strftime('%H:%M:%S')}.\n")
formulateDt()