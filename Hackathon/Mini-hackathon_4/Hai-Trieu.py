#Phần 1
#bài 1:
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
soluongMacBook = in4["MACBOOK"]
print(f"Available MACBOOKs: {soluongMacBook}")

#Bài 3:
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
nhap_hang = input("Input a brand: ")
soluong = in4.get(nhap_hang.upper(), 0)
print(f"Available {nhap_hang.upper()}: {soluong}")


#Phần 2:
#Bài 1:
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

in4.update({"TOSHIBA" : 10})
print(f"Available products:")
for in4, soluong in in4.items():
    print(f"{in4}: {soluong}")


#Bài 2:
in4 = {}

Soluong_Product = int(input("Input amount of products: "))

for i in range(Soluong_Product):
    Name_Product = input("Input a brand: ")
    Num_Product = int(input("Input amount: "))
    in4[Name_Product] = Num_Product

print("Available products:")
for Name_Product, Num_Product in in4.items():
    print(f"{Name_Product}: {Num_Product}")


#Bài 3:
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

in4['DELL'] = in4['DELL'] + 10
in4['MACBOOK'] = in4['MACBOOK'] - 10
print("Available products:")

for Name_Product, Num_Product in in4.items():
    print(f"{Name_Product}: {Num_Product}")


#Bài 4 :
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

total_numofproducts = 0
for Name_Product, Num_Product in in4.items():
    total_numofproducts += Num_Product

print("Total products:", total_numofproducts)



#pHẦN 3:
#Bài 1+2:
in4 = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}

Price_ASUS = in4["ASUS"]
print(f"Price of ASUS: {Price_ASUS}")

#Bài 3:
in4 = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}
nhap_hang = input("Input a brand: ")
Price = in4.get(nhap_hang.upper(), 0)
print(f"Price of {nhap_hang.upper()}: {Price}")


#Phần 4:
#Bài 1:
in4 = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}
num_ofasus = 5
totalprice_of5asus = num_ofasus * in4["ASUS"]
print(f"Total price: {totalprice_of5asus}")

#Bài 2:
in4 = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}
name = input("Input a brand: ")
num = int(input("Input amount to buy: "))

totalprice = num * in4[name]
print(f"Total price: {totalprice}")

#Bài 3:
prices = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}
def xuat_kho(name, num):
    global total_price

    if name in in4:
        if num <= in4[name]:
            price = prices[name]
            total_price = num * price
            
            in4[name] -= num
        else:
            print("Not enough product!")
            return
    else:
        print("There aren't any product in shop!")
        return 
    print(f"Total price: {total_price}")


name_update = input("Input a brand: ")
num_update = int(input("Input amount "))

xuat_kho(name_update, num_update)

print("Available products:")
for name, num in in4.items():
    print(f"{name} in shop: {num}")



#Phần 5:
#Bài 1"
prices = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

total_values = {}

for name, num in in4.items():
    if name in prices:
        total_values[name] = prices[name] * num 
    else:
        print("Error!")
print("Total value of available brands: ")
for name, value in total_values.items():
    print(f"{name}: {value}")

#Bài 2:
prices = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS" : 400
}
in4 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
}

total_value = 0
for name, num in in4.items():
    if name in prices:
        total_value += prices[name] * num
print("Total value of available items:", total_value)


#Phần 6:
#Bài 1+2:
Character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 10,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}
Character["Gold"] = Character.get("Gold", 0) +50
print(f'Gold: {Character["Gold"]}')


#Bài 3:
Character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 10,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}
Character["Backpack"].append("FlintStone")
print(f"Backpack: {Character['Backpack']}")