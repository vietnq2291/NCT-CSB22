#Bài 1:
print("Đây là bài 1: ")
Numb = int(input("Input number: "))
for x in range(Numb):
    print("#" * (x+1)) 


#Bài 2:
print("Đây là bài 2: ")
while True: 
    SoDuong = float(input("Input a positive number: "))
    if SoDuong > 0: 
        print("Thank you.")
        break


#Bài 3:
print("Đây là bài số 3:")
Number = int(input("Input number: "))
if Number >= 1:
    t = 1
    for x in range(1, Number+1):
        t = t * x
    print(f"{Number}! = {t}")
elif Number == 0:
    print(f"0! = 1")
else:
    print("Invalid")



#Bài 4:
print("Đây là bài số 4:")
Number = int(input("Input number: "))
t = 0
for x in range(len(str(Number))):
    t += int(str(Number)[x])
print(t)



#Bài 6:
print("Đây là bài số 6:")
print("Please input the box below number > 2")
canh = int(input("Number of edges: "))
if canh > 2:
    if canh == 3: 
        rotDeg = 180 - (180/canh)
        print(rotDeg)
        for x in range(canh):
            import turtle as t
            t.forward(100)
            t.right(rotDeg)
    elif canh > 3:
        rotDeg = 360 - (canh-1)*(360/canh)
        print(rotDeg)
        for x in range(canh):
            import turtle as t
            t.forward(100)
            t.right(rotDeg)



#Bài 7:
print("Đây là bài số 7: ")
r = 0
while True: 
  r += 10
  import turtle as t
  t.circle(r, 180, 10)   
  if r == 180:
   break