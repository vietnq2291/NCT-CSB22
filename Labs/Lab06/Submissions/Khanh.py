#Bài 1
arr = [0,1,2,3,4,5,6,7,8,9]
arr1 = []
arr2 = []
for i in arr:
    arr1.append(i + 2)
print(arr1)
for x in arr:
    arr2.append(x*2)
print(arr2)
arr.remove(0)
arr.remove(1)
arr.extend([0,1])
print(arr)
#Bài 2
arr = ["l", "o", "o", "h", "c", "s", " ", "y", "g", "o", "l", "o", "n", "h", "c", "e", "T", " ", "X", "d", "n", "i", "M"]
arr.reverse()
print(arr)
#Bài 3
arr = [1,1]
a = 0 
n = int(input())
for i in range(n-2):
    a = arr[i]+ arr[i+1]
    arr.append(a)
print(arr)
#Bài 4
a = 0
arr = [(30.5, 'Steak'), (5, 'Salad'), (7, 'Wine'), (12, 'Salmon'), (8.5, 'Soup'), (4.5,'Cake')]
arr1 = [30.5, 5, 7, 12, 8.5, 4.5]
for i in arr1:
    a = a+i
b = a/6
print(f'{b} là giá trung bình')
for x in range(len(arr1)):
    if arr1[x] > b:
        print(f'Món lớn hơn giá trung bình {arr[x]}')
#Bài 5
input_str = input()
word_list = input_str.split()
word_list.sort()
for i in word_list:
    if word_list.count(i) > 1:
        word_list.remove(i)
        if i in word_list:
            continue
print(len(word_list))
