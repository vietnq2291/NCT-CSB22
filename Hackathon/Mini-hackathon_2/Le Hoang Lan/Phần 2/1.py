list = ['blue', 'red', 'teal', 'green']
print("Color list: ",*list)
x=int(input("Input position: "))
print(f"Color at position {x}: {list[x-1]}")