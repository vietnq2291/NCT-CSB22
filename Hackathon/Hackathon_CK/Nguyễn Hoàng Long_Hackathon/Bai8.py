n = int(input("Nhập số nguyên > 0:"))
a, b = 1, 1
fib_sequence = [a, b]

while len(fib_sequence) < n:
    a, b = b, a +b
    fib_sequence.append(b)

print("các",n ,"Phần tử đầu tiên của dãy fibonacci:")
print(*fib_sequence)


