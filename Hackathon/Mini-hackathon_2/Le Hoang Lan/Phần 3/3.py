sum = 0
while True:
    list = int(input("Input the list of numbers \n Enter 0 to finish. \n"))
    if list != 0:
        sum += list
    else:
        break
print("Sum of all numbers: ",sum)