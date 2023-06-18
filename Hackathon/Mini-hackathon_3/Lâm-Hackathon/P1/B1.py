def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
        
num = int(input("Input a number: "))
if is_even(num) == True:
    print("This number is even")
else:
    print("This number is not even")
