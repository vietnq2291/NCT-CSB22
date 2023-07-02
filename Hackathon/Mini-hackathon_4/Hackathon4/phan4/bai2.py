price_table = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

hang_may = input("Nhập hãng máy: ")
so_luong = int(input("Nhập số lượng: "))

gia_mot_may = price_table.get(hang_may, 0)
tong_gia_tri_don_hang = gia_mot_may * so_luong

print(f"Total price: {tong_gia_tri_don_hang}")
