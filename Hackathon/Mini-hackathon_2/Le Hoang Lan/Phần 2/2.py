mylist = ['blue', 'red', 'teal', 'green']
print("Color list: ",*mylist)
x= input("Item to delete: ")
if x.isdigit() :
    del mylist[int(x)]
elif x in mylist:
    mylist.remove(str(x))
print('New color list: ',*mylist)
