def restaurant_order():
    menu = ["bún bò", "phở", "miến", "mỳ gà", "cơm tấm"]
    order = []

    while True:
        dish = input("Vui lòng chọn món ăn: ")
        if dish.lower() in order: 
            print("Món ăn này đã được gọi.")
        elif dish.lower() in menu:  
            order.append(dish.lower()) 
            print("Đã thêm món ăn vào danh sách.")
        else:
            print("Món ăn không có trong menu.")
        more_dish = input("Có muốn đặt thêm không? (y/n): ")
        if more_dish.lower() != 'y':
            break
    print("Những món đã đặt:")
    for dish in order:
        print("- " + dish)


print("== Welcome to MindX Restaurant ==")
restaurant_order()
