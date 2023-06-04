list = [1,3,0,8]
x= int(input("Input a number:  "))
if x in list:
    print ("Number found at position ",list.index(x))
else:
    print('Number not found')
