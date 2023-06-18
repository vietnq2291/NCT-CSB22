def print_fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end=' ')
        a, b = b, a + b
        
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
print_fibo(n)
10