#BT1
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # thường 
print ("Original list: ",arr)
arr_1 = arr
for x in range (len(arr_1)): # cộng 2 
    arr_1[x] = x + 2
print ("Add 2: ",arr_1)

arr_2 = arr
for x in range (len(arr_2)): # nhân 2 
    arr_2[x] = x * 2
print ("Multiply by 2: ",arr_2)

arr_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # dịch sang 2
del (arr_3[0])
del (arr_3[0])
arr_3 [10:10] = [0, 1]
print ("Shift 2:", arr_3)

#BT2
MindX = ['l', 'o', 'o', 'h', 'c', 'S', '', 'y', 'g', 'o', 'l', 'o', 'n', 'h', 'c', 'e', 'T', '', 'X', 'd', 'n', 'i', 'M' ]
MindX.reverse()
print (MindX)

#BT3
n = int(input("Input a positive number: "))
a = 1 
b = 1 
Fibonacci_series = [1,1]
for x in range (2,n):
 next = Fibonacci_series [x-1] + Fibonacci_series [x-2]
Fibonacci_series.append (next)
print ("First", n, "Fibonacci numbers: ",Fibonacci_series)
# Câu này e ch hiểu s k đúng ạ

#BT4
Num = int(input ("Number of items: "))
total_price = 0
for x in range(0,Num):
 a = input(f'Item {x+1}: ')
 b = float(input(f"Price of Item {x+1}: "))
 total_price += b
print ("Average price: ",total_price/(x+1))
c = [b]
d = (a,b)
selected_food = ""
for x in range (0,Num):
    if b > total_price/(x+1):
        selected_food += f"{a}"
print (selected_food)
        
#BT5

sentence = input("Write a sentence: ")
sentence.lower()
used_words = []
count = 0 
words = sentence.split()
for x in words:
    if x not in used_words:
     used_words.append(x)
     count += 1
print("Number of unique words: ",count)
     
 
 
 

         