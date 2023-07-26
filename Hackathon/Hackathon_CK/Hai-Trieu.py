#Bài 1:
num_1 = int(input("Input first number: "))
num_2 = int(input("Input second number: "))
sum = num_1 + num_2
print(f'{num_1} + {num_2} = {sum}')


#Bài 2
import math
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("input c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("This equation has 2 olutions:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("This equation has double solutions:")
    print("x =", x)
else:
    print("This equation doesn't have any solutions.")


#Bài 3:
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False
    
string = input("Input a text: ")

if is_palindrome(string):
    print("This is a palindrome".format(string))
else:
    print("This is not a palindrome".format(string))


#Bài 4:
print("== Welcome to MindX Restaurant ==")
def nv_phucvu():
    monduocgoi = []
    
    while True:
        item = input("Please choose a dish: ")
        
        if item in monduocgoi:
            print("You choose this already.")
        else:
            monduocgoi.append(item)
        
        add_food = input("Anything else? (C/K): ")
        if add_food.upper() == "K":
            break

    print("Well done! Your order:")
    for item in monduocgoi:
        print(item)

nv_phucvu()



#Bài 5:
Prices_ofPhones = {
    'Iphone12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000,
    'Vivo': 4200000
}

name_phone = input("Input name of a phone: ")

if name_phone in Prices_ofPhones:
    price = Prices_ofPhones[name_phone]
    print(f"Price of {name_phone} là {Prices_ofPhones}")
else:
    print("There isn't any ìnormation about this phone!")

Budget = int(input("Input your budget: "))
suitable_phones = [phone for phone, price in Prices_ofPhones.items() if price <= Budget]

if suitable_phones:
    print(f"Phones that fit your budget:")
    for phone in suitable_phones:
        print(phone)
else:
    print("There aren't any phones that fir your budget!")


#Bài 6:
num = int(input("Input a umber (> 0): "))
num_str = str(num)
num_digits = len(num_str)
print(f"This number has {num_digits} digit(s).")



#Bài 7:
def sort_list(nums):
    n = len(nums)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [5, 1, 8, 92, -1, 30]

print("Original list:")
print(nums)

sort_list(nums)

print("Sorted list:")
print(nums)



#Bài 8:
def Fibonacci(n):
    already_know = [1, 1]

    for i in range(2, n):
        next_num = already_know[i - 1] + already_know[i - 2]
        already_know.append(next_num)

    return already_know

n = int(input("Input a numbe ( > 0 ): "))

while n <= 0:
    n = int(input("Input a number again ( > 0 ): "))

already_know = Fibonacci(n)
print(f"First {n} Fibonacci numbers: ")
print(already_know)
