list = [1,3,0,8,4]
y =""
for x in list:
    if x % 2 ==0:
        y += f" {x}"
    else: continue
print("Even numbers:",y)