#Phần 1
#Bài 1
def chan(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Input a number: "))
if chan(num):
    print("This number is even")
else:
    print("This number is not even")




#Bài 2:
def cal_area(bkinh):
    PI = 3.14
    area = PI * bkinh ** 2
    return area

bkinh = float(input("Input radius: "))
area = cal_area(bkinh)
print("Circle’s area:", area)


#Bài 3
def reverse_str(chuoi):
    return chuoi[::-1]
input_chuoi = input("Input a text: ")
dao_chuoi = reverse_str(input_chuoi)
print("Reversed text:", dao_chuoi)


#Bài 4:
def is_palindrome(chuoi):
    if chuoi == chuoi[::-1]:
        return True
    else:
        return False
input_chuoi = input("Input a text: ")
if is_palindrome(input_chuoi):
    print("This is a palindrome.")
else:
    print("This isn't a palindrome.")



#Phần 2:
def hamso(n):
    if n <= 0:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
n = int(input("Input a number: "))
fact = hamso(n)
print(f"{n}! = {fact}")


#Bài 2
def list(day):
    n = len(day)
    for i in range(n):
        for j in range(0, n-i-1):
            if day[j] > day[j+1] :
                day[j], day[j+1] = day[j+1], day[j]

day = [5, 1, 8, 92, -1, 30]
list(day)
print("Sorted list:", day)


#Bài 3
def print_fibo(n):
    a, b = 1, 1
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
n = int(input("Input a number: "))
print_fibo(n)


