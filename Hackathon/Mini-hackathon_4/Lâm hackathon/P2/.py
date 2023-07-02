# Bài 1
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
computer_brand["TOSHIBA"] = 10
print("Available products:")
for br, it in computer_brand.items():
    print(f"- {br}: {it}")

# Bài 2
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
brand = input("Input a brand: ")
amount = int(input("Input amount: "))
computer_brand[brand] = amount
print("Available products:")
for br, it in computer_brand.items():
    print(f"- {br}: {it}")

# Bài 3
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
computer_brand["DELL"] = 60
computer_brand["MACBOOK"] = 2
print("Available products:")
for br, it in computer_brand.items():
    print(f"- {br}: {it}")

# Bài 4
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
print(f"Total products: {sum(computer_brand.values())}")