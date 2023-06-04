a = 0
count = 0
arr = [(30.5, 'Steak'), (5, 'Salad'), (7, 'Wine'), (12, 'Salmon'), (8.5, 'Soup'), (4.5,'Cake')]
arr1 = [30.5, 5, 7, 12, 8.5, 4.5]
print("Number of items: 6")
for i in arr1:
        a = a + i
b = a/6
print("Average price: ", b)
for j in arr1:
    if j > b:
          count= count +1
          k=arr1.index(j)
          print(f"Item(s) above average price: ", arr[k])