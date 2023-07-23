comp = ['Iphone12: 28000000', 'Samsung N10: 16000000', 'Oppo 93: 7500000', 'Vsmart: 7400000', 'Vivo: 4200000']
gia = [28000000,16000000,7500000,7400000,4200000]
budget = int(input("Input your budget: "))
print("Phones that fit your budget: ")
arr=[]
for i in gia:
    if i <= budget:
        a=gia.index(i)
        b = comp[a]
        arr.append(b)
print(*arr)
