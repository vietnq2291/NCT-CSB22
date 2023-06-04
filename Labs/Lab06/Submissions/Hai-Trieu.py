#Bài 1
day_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
day_2 = []
day_3 = []
day_4 = []

for x in day_1:
    day_2.append(x+2)
for y in day_1:
    day_3.append(y*2)
day_4 = day_1[2:] + day_1[:2]

print(day_2, "\n", day_3, "\n", day_4)


#Bài 2
day = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l', 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']

sapxep_day = ''.join(day[::-1])
print(sapxep_day)


#bài 3
n = int(input("Nhập số phần tử của dãy Fibonacci: "))
a, b = 1, 1
print("Dãy Fibonacci với", n, "phần tử là:")
print(a)
print(b)

for i in range(n-2):
    c = a + b
    a = b
    b = c
    print(c)


#bài 4
n = int(input("Số lượng món ăn: "))

menu = []

for i in range(n):
    item = input(f"Tên món ăn {i+1}: ")
    price = float(input(f"Giá {i+1}: "))
    menu.append((item, price))

total_price = sum([item[1] for item in menu])
gia_tb = total_price / n

tren_tb = [item for item in menu if item[1] > gia_tb]

print(f"Giá trung bình: {gia_tb}")
print("Món ăn trên trung bình:", end=" ")
for item in tren_tb:
    print(item, end=" ")


#Bài 5
input_str = input("Write a sentence: ")
word_list = input_str.split()
unique_words = set(word_list)
num_unique_words = len(unique_words)
print("Number of unique words:", num_unique_words)


