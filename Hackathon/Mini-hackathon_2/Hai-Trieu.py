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


#---------#
numbers = int(input("Input the amount of number: "))
list_numbers = []
for i in range(numbers):
    number = int(input("Input number: "))
    list_numbers.append((number))
for number in list_numbers:
    if number % 2 == 0:
        print("Even numbers:", number)