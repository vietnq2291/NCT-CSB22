# # Mini Hackathon 2 
# # Part 1 
# Init_color = ["blue", "red", "green"] 
# print ("Color list:", *Init_color, sep = ",")
# # Add
# New_color = input("Input a new color: ")
# Init_color.append(New_color)
# print ("New color list: ",*Init_color, sep = ",")

# # Part 2 
# # Index
# position = int(input("Input position: "))
# print (Init_color[position])
# # Delete
# position_1 = input("Item to delete: ")
# if position_1.isdigit():
#     Init_color.pop (int(position_1))
#     print (*Init_color, sep = ",")
# else:
#     Init_color.remove (position_1)
#     print (*Init_color, sep = ",")

# # Draw
# from turtle import *
# for x in Init_color:
#  Turtle.color(Init_color[x])
#  Turtle.forward (50)
#  Turtle.penup ()
#  Turtle.forward(20)
#  Turtle.pendown()

# Part 3 
# num_list = [7,45,-98,30,122,-157]
# num_input = float(input("Input a number: "))
# if num_input in num_list:
#     print ("Number found at position", (num_list.index(num_input)) + 1)
# else: 
#     print ("Number not found")

# sum = 0 
# for x in num_list:
#     sum += int(x) 
# print ("Sum of all numbers: ", sum)

# print ("Input the list of numbers.")
# print ("Enter 0 to finish.")
    
# num_list2 = []
# sum2 = 0
# typed_num = input ("") 
# while True:
#     if typed_num != 0:
#      num_list2.append (typed_num)
#     elif typed_num == 0:
#      for x in num_list2: 
#       sum2 += int(x) 
#     break

# print ("Sum of numbers in list: ",sum2)

# # Part 4
# num_list3 = [2,4,78,90,23,53,-100]
# even_num = []
# for x in num_list3:
#     if x % 2 == 0: 
#         even_num.append (x)
   
# print ("Even numbers: ",even_num)


# num_list4 = []
# even_num_list = []
# typed_num1 = input ("") 
# while True:
#     if typed_num1 != 0:
#      num_list4.append (typed_num1)
#     else:
#         for x in num_list4:
#             if x %2 == 0:
#                 even_num_list.append(x)
      
#     break

# print ("Even numbers in list: ",even_num_list)

# # Part 5
# Dist_name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
# Dist_pop = [247100, 333300, 266800, 420900, 318000]
# print ("Indices of:")
# print ("Most populated dist: ",Dist_name.index("ĐĐ") + 1)
# print ("Least populated dist: ",Dist_name.index("BĐ") + 1)
# print ("Names of:")
# print ("Most populated dist: ",Dist_name [3]) 
# print ("Least populated dist: ",Dist_name [0])

# # Part 6
# Dist_area = [9.224, 43.35, 12.04, 9.96, 10.09]
# Dist_density = []
# for x in Dist_pop:
#     Dist_density.append (int(x) / Dist_area [Dist_pop.index (x)])
# print ("Population density of:")
# for y in Dist_name:
#     print (f'- {y}: {Dist_density[Dist_name.index(y)]}')
    
# print ("Average population density: ")
# sum_density = 0
# for z in Dist_density:
#     sum_density += int(z)
# print (sum_density/5)

# Part 7
high_score = [100,123,257,390]
print ("High scores: ")
for x in high_score:
    print (f'{high_score.index(x) + 1}. {x}')

# Part 8
high_score = [100,123,257,390]
print ("High scores: ")
high_score.reverse()
for x in high_score:
    print (f'{high_score.index(x) + 1}. {x}')

new_high_score = [100,123,257,390,1004,1598,765,349]
new_score = int (input("Input a new score: "))
new_high_score.append (new_score)
new_high_score_sorted = sorted(new_high_score)
new_high_score_sorted.reverse()
scores_on_screen = 0
for x in new_high_score_sorted:
    print (f'{new_high_score_sorted.index(x) + 1}. {x}')
    scores_on_screen += 1 
    if scores_on_screen == 5:
        break

    

        
        
 


