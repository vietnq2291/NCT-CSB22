import random

def search_number():
    my_list = random.sample(range(1, 20), random.randint(6, 10))
    print("List của bạn là:", my_list)
    number = int(input("Nhập vào một số: "))
    try:
        index = my_list.index(number) + 1
        print(f"Số này có trong list và đứng ở vị trí thứ {index}")
    except ValueError:
        print("Số này không có trong list")

search_number()
