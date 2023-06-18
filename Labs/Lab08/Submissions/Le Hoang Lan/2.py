num = int(input("Input number: "))
def is_prime(num):
    count = 0
    for i in range(1,num):
        num%i == 0
        count +=1
    if count == 2:
        return True
    else:
        return False
if is_prime(num):
    print(f"{int(num)} is a prime.")
else: 
    print(f"{num} is a not prime.")

