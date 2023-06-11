#Phần 1
colors = ["blue", "red", "green", "teal"]
for color in colors:
    print(color)
new = input("Input a new color: ")
new_colors = colors.append(new)
print(colors)


#Phần 2
colors = ["blue", "red", "green", "teal"]
num = int(input("Input position: "))
print("Color at position",num, ":", colors[num + 1])
#--------------#
colors = ["", "blue", "red", "green", "teal"]
delete = input("Item to delete: ")
if delete.isdigit():
    index = int(delete)
    if index < len(colors):
        colors.pop(index)
    else: 
        print("Cannot find position", index, "in list!")
else:
    try:
        colors.remove(delete)
    except ValueError:
        print("Cannot find position", delete, "in list!")
print("New color list:", colors)
#-----------#
import turtle as t
colors = ["red", "green", "violet", "purple"]
t.pensize(5)
t.speed(4)
for color in colors:
    t.pencolor(color)
    t.forward(40)
t.done()




#Phần 3:
numbers = [5, 1, 8, 92, -1, 30]
search_number = int(input("Nhập vào 1 số: "))
try:
    position = numbers.index(search_number)
    print("Number found at posiotion: ", position + 1)
except ValueError:
    print("Number not found!")

#---------#
numbers = [5, 1, 8, 92, -1, 30]
total = sum(numbers)
print("Sum of all numbers:", total)

#----------#
numbers = int(input("Input the amount of number: "))
list_numbers = []
for i in range(numbers):
    number = int(input("Input number: "))
    list_numbers.append((number))
sum_num = sum(list_numbers)
print("Sum of numbers in list:", sum_num)


#Phần 4
numbers = int(input("Input the amount of number: "))
list_numbers = []
for i in range(numbers):
    number = int(input("Input number: "))
    list_numbers.append((number))
for number in list_numbers:
    if number % 2 == 0:
        print("Even numbers:", number)

#Phần 5:
quan_in4 = {
    'BĐ': {'area': 9.224, "population": 247100},
    'BTL': {'area': 43.35, "population": 333300},
    'CG': {'area': 12.04, "population": 266800},
    'ĐĐ': {'area': 9.96, "population": 420900},
    'HBT': {'area': 10.09, "population": 318000},
}
list_quan = []
population = []
for cacquan, in4 in quan_in4.items():
    list_quan.append(cacquan)
    population.append(in4['population'])
print("Danh sách các quận của quận: ", list_quan)
print("Danh sách dân số của các quận: ", population)
highest_ppl_thutu = population.index(max(population))
lowest_ppl_thutu = population.index(min(population))
print("-Về dân cư:")
print("Số thứ tự của",list_quan[highest_ppl_thutu], "nơi có số dân cao nhất:", highest_ppl_thutu)
print("Số thứ tự của",list_quan[lowest_ppl_thutu], "nơi có số dân thấp nhất:", lowest_ppl_thutu)



#Phần 6:
city_in4 = {
    'BĐ': {'area': 9.224, 'population': 247100},
    'BTL': {'area': 43.35, 'population': 333300},
    'CG': {'area': 12.04, 'population': 266800},
    'ĐĐ': {'area': 9.96, 'population': 420900},
    'HBT': {'area': 10.09, 'population': 318000}
}

list_matdods = []
tong_matdods = 0
for cacquan, in4 in city_in4.items():
    matdods = in4['population'] / in4['area']
    list_matdods.append(matdods)

    tong_matdods += city_in4[cacquan]['population'] / city_in4[cacquan]['area']

soluong_quan = len(city_in4)
trungbinh_matdods = tong_matdods / soluong_quan

print("Danh sách mật độ dân số của các quận:", list_matdods)
print("Mật độ dân số trung bình của các quận là:", trungbinh_matdods)

#Phần 7+8: 
high_scores = [78, 56, 67, 89, 73]
new_score = int(input("Nhập điểm mới của bạn: "))
high_scores.append(new_score)
high_scores.sort(reverse=True)
top5_scores = high_scores[0:5]
for score in top5_scores:
    print( score)




