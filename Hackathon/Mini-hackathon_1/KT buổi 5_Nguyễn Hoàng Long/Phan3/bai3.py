month = int(input("Nhập một tháng trong năm (1 đến 12): "))

if month == 2:
    year = int(input("Nhập một năm: "))
    if (year % 4 == 0 and year % 100 != 0):
        days = 29
    else:
        days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    days = 31

print("Tháng", month, "có", days, "ngày")
