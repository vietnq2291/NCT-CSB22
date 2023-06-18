iList = [5, 1, 8, 92, -1, 30]

for x in range(len(iList)):
    for y in range(x+1, len(iList)):
        if iList[x] > iList[y]:
            iList[x] = iList[y]
print(iList)


#Part 2:
def print_fibo(n):
    count = 0
    base = 0
    n1 = 1
    n2 = 1
    if n > 0: 
        while count < n:
            base = n1 
            n1 = n2 
            n2 = base + n1
            print(n2)
            count += 1
print_fibo(5)



def calc(num):
    base = 1
    for x in range(1, num+1):
        base *= x
    print(f"{num}! = {base}")

calc(5)


#Part 1: 
def evenNum(num):
    if num%2==0:
        print("This number is even.")
        return True
    else:
        print("This number is not even.")
        return False

uInput1 = int(input("Input a number: "))

def cal_area(r):
    area = ((3.14)*(r**2))
    print(f"Circle's area: {area}")
cal_area(1)

def reverse_str(uStr):
    reversedStr = uStr[::-1]
    print(reversedStr)
reverse_str("mindX")

def is_palindrom(uStr):
    if uStr == uStr[::-1]:
        print("This is a palindrome.")

is_palindrom("anna")