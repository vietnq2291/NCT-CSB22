colors = ["blue", "red", "teal", "green"]
position = int(input("Nhập vị trí của màu bạn muốn xem (1-4): ")) - 1

if position in range(len(colors)):
    color = colors[position]
    print("Màu ở vị trí", position + 1, "là:", color)
else:
    print("Vị trí không hợp lệ")
