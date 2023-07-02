price_table = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

hang_may = input("Nhap ten hang may: ")

print(f"Gia cua mot may {hang_may}: {price_table.get(hang_may, 'Khong tim thay')}")

