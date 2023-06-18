# # Part 1
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else: 
#         return False

# num1 = int (input("Input a number: "))
# if is_even(num1):
#     print ("This number is even")
# else: 
#     print ("This number is not even")
    
# def cal_area(n):
#     return n*n*3.14

# num2 = int (input("Input radius: "))
# print ("Circle's area:",cal_area(num2))

# def reverse_str(n):
#     reversed_text = ''
#     for char in n: 
#         reversed_text = char + reversed_text
#     return reversed_text
    
# text1 = input ("Input a text: ")

# print ("Reversed text:",reverse_str(text1))

# def palindrome (n):
#     reversed_text = ''
#     for char in n: 
#         reversed_text = char + reversed_text
#     if reversed_text == n:
#         return True 
#     else: 
#         return False

# text2 = input ("Input a text: ")
# if palindrome (text2):
#     print ("This is a palindrome.")
# else: 
#     print ("This is not a palindrome.")
    
# Part 2

# def factorial (n):
#     factor = 1
#     for i in range (1,n+1):
#         factor = factor * i 
#     return factor 

# num3 = int (input("Input a number: "))
# print (f'{num3}! = {factorial(num3)}')
                
# list1 = [5,1,8,92,-1,30]
# print ("Original list: ",list1)
# a = len(list1)
# for i in range (0, a - 1):
#     for k in range (i+1, a):
#        if list1 [k] < list1 [i]:
#             x = list1 [i]
#             list1 [i] = list1 [k]
#             list1 [k] = x

# print ("Sorted list: ",list1)

# def print_fibo (n):
#  if n <= 0:
#      return None
#  if n == 1:
#      return 1
#  else: 
#      Fibo_arr = [1,1]
#      next = 0 
#      for i in range (2,n):
#          next = Fibo_arr [i-1] + Fibo_arr [i-2]
#          Fibo_arr.append (next)
#      return (Fibo_arr)  
       
   
       
# num4 = int(input("Input a number: "))
# print ("First",num4,"Fibonacci numbers:",print_fibo(num4))

# Part 3 
import os 
os.system ('cls')
import msvcrt
ch = msvcrt.getch().decode ('utf - 8')

line1 = ['P','-','-','-','-','-','-','-','-','-']
line2 = ['-','-','-','-','-','K','-','-','-','-']
line3 = ['-','-','-','-','-','K','-','-','-','-']
line4 = ['D','-','-','-','-','-','-','-','-','-']
line5 = ['-','-','-','-','-','-','-','-','-','-']
        
print (line1)
print (line2)
print (line3) 
print (line4) 
print (line5)
print ('')
print ("== THE ESCAPE GAME ==")
print ("Use W A S D to move (P)layer")
print ('Find (K)ey first then exit through the (D)oor')

              