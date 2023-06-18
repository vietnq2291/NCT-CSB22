def print_fibo(x):
    if x <= 0:
        print("You have to enter a number greater than 0")
        return
    elif x == 1:
        f1 = [1]
    elif x == 2:
        f1 = [1, 1]
    else:
        f1 = [1, 1]
        for i in range(2, x):
            f2 = f1[i-1] + f1[i-2]
            f1.append(f2)
    
    for num in f1:
        print(num, end=" ")

fibo_input = int(input("Input a number: "))
print_fibo(fibo_input)