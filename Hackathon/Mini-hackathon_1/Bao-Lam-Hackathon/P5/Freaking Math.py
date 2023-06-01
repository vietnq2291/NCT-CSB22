import random


print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores.")
n1 = random.randint(1,100)
n2 = random.randint(1,100)

while True:
    print(f"{n1} + {n2} = ")
    if n1 + n2 == random.randint(-100,200):
        print("2")
