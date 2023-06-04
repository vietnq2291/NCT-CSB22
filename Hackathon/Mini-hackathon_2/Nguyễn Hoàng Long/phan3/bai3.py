numbers = []
number = int(input("Nhập số: "))
while number != 0:
    numbers.append(number)
    number = int(input("Nhập số tiếp theo, nhập 0 để kết thúc: "))

print("Danh sách số của bạn là:", numbers)
print("Tổng của danh sách là:", sum(numbers))
