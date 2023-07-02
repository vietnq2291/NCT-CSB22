# Bài 1
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}

# Bài 2
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
print(f"Available MACBOOKs: {computer_brand['HP']}")

# Bài 3
computer_brand = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}
user_input = input("Input a brand: ")
if user_input in computer_brand.keys():
    print(f"Available {user_input}s: {computer_brand[user_input]}")
else:
    print("Not available")