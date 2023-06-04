# B1
arr = ["blue", "red", "teal", "green"]
print(f"Color list:\n{arr}")
inp = int(input("Input position: "))
color = arr[inp - 1]
print(f"Color in position {inp}: {color}")

# B2
arr = ["blue", "red", "teal", "green"]
print(f"Color list:\n{arr}")
del_item = input("Item to delete: ")
if del_item.isdigit() : 
    del(arr[int(del_item) - 1])
else:
    arr.remove(del_item)
print(arr)

# B3
import turtle as t
