phone_prices = {
    "Iphone12": 28000000,
    "Samsung N10": 16000000,
    "Oppo 93": 7500000,
    "Vsmart": 7400000,
    "Vivo": 4200000
}

while True:
    print("1. Tìm giá điện thoại")
    print("2. Tìm điện thoại theo ngân sách")
    print("3. Thoát")
    choice = input("Lựa chọn của bạn: ")

    if choice == "1":
        phone_name = input("Nhập tên điện thoại: ")
        if phone_name in phone_prices:
            print(f"Giá của {phone_name} là: {phone_prices[phone_name]}")
        else:
            print("Không tìm thấy giá của điện thoại này.")
    elif choice == "2":
        budget = int(input("Nhập số tiền dự tính để mua điện thoại: "))
        offer_phones = [phone_name for phone_name, price in phone_prices.items() if price <= budget]
        if offer_phones:
            print("Các điện thoại có mức giá phù hợp:")
            for phone_name in offer_phones:
                print("- " + phone_name)
        else:
            print("Không có điện thoại nào phù hợp với số tiền dự tính của bạn.")
    elif choice == "3":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

print("Cảm ơn bạn đã sử dụng chương trình.")
