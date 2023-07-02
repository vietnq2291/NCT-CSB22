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

tong_gia_tri = {}

for hang, so_luong in product_quantity.items():
    gia_mot_may = price_table.get(hang, 0)
    tong_gia_tri[hang] = gia_mot_may * so_luong

print("Tổng giá trị từng hãng trong kho:")
for hang, gia_tri in tong_gia_tri.items():
    print(f"- {hang}: {gia_tri}")
