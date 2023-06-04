y=""
while True:
    list = int(input("Input the list of numbers \n Enter 0 to finish. \n"))
    if list != 0:
        if list % 2 == 0:
            y += f"{list}"
        else:
            continue
    else: break
print("Even numbers in list: ",y)