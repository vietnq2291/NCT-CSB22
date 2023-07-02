computer_inventory = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

brand = input("Nhap vao ten loai may: ")
amount = int(input("Nhap vao so luong: "))

computer_inventory[brand] = amount

print("Products:")
for brand, quantity in computer_inventory.items():
    print(f"- {brand}: {quantity}")
