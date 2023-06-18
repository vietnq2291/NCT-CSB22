n = int(input("Input a number: "))
def even(n):
    if n %2 ==0:
        return True
    else:
        return False
    
if even(n):
    print("This number is even")
else: 
    print("This number is not even")

