list = ['blue', 'red', 'teal', 'green']
print("Color list: ",*list)
list2 = input("Input a new color:")
list.append(list2)
print("New color list: ", *list)