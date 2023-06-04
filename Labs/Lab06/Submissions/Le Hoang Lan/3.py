n =int(input("Input a positive number: "))
a1= 0 
a2= 1
g = ""
for x in range(1,n):
    a = a1 + a2
    a1 = a2
    a2 = a
    g += f" {a}"
print(f"First {n} Fibonacci number(s): {g}")     