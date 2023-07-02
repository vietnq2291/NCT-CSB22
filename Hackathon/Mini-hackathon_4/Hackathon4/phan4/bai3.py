price_table = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

product_quantity = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

hang_may = input("Nhập hãng máy: ")
so_luong_xuat_kho = int(input("Nhập số lượng: "))

tong_gia_tri_xuat_kho = price_table.get(hang_may, 0) * so_luong_xuat_kho
product_quantity[hang_may] -= so_luong_xuat_kho

print(f"Total price: {tong_gia_tri_xuat_kho}")
print("Available products:")
for hang, so_luong in product_quantity.items():
    print(f"- {hang}: {so_luong}")
