sls = int(input("Input number: "))

def is_prime(n):
    count1 = 0
    for i in range(1,n):
        n%i == 0
        count1 +=1
    if count1 == 2:
        return True
    else:
        return False
count2 = 0
n = 2
s = ""
while count2 < sls + 1:
    if is_prime(n):
        s += f" {n}"
    else: count2 +=1
    n += 1

print(f"First 9 prime(s): {s}")




