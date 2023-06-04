colors = ["blue", "red", "teal", "green"]
print("danh sách các màu:",colors)
value= input("màu muốn xoá:")
colors.pop(int(value) - 1) if value.isdigit() else colors.remove(value)
print("Danh sách các màu còn lại:",colors)