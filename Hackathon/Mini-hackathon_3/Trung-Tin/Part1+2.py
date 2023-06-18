
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

#Part 2:
def calc(num):
    base = 1
    for x in range(1, num+1):
        base *= x
    print(f"{num}! = {base}")
calc(5)

numList = [5, 1, 8, 92, -1, 30]
def sortList(uList):
    count = 0
    sortedList = []
    while uList:
        min = uList[0]  
        for x in uList: 
            if x < min:
                min = x
        sortedList.append(min)
        uList.remove(min)    
        count += 1
    print(sortedList)
sortList(numList)

def print_fibo(n):
    count = 0
    n1 = 0
    n2 = 1
    res = ""
    if n > 0: 
        while count < n:
            n3 = n1 + n2
            n1 = n2 
            n2 = n3
            res += f" {str(n3)}"
            count += 1
    print(res)
print_fibo(5)

