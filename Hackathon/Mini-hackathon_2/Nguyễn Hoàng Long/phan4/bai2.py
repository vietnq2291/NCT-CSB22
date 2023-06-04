numbers = []
while True:
    number = int(input("Nhập số, nhập 0 để kết thúc: "))
    if number == 0:
        break
    numbers.append(number)

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print("các số chẵn trong danh sách:", even_numbers)
