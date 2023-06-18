n = int(input("Input a number: "))
giai_thua = 1

for i in range(1, n+1):
    giai_thua *= i

print("{0}! = {1}".format(n, giai_thua))
