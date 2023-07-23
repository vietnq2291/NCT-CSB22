import math
a= float(input("Input number a: "))
while True:
    if a == 0:
        a = float(input("Số a phải khác 0: "))
    else:
        break
b = int (input("Input second number b: "))
c = int (input("Input second number c: "))
delta = b*b-4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )