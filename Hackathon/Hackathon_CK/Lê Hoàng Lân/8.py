n = int(input("Input a number: "))
if n < 0:
    print(" n must > 0")
def print_fibo(n):
    a1= 0 
    a2= 1
    g = ""
    for x in range(n-1):
        a = a1 + a2
        a1 = a2
        a2 = a
        g += f" {a}"
    return g
print(f"First {n} Fibonacci number(s): 1{print_fibo(n)}")   