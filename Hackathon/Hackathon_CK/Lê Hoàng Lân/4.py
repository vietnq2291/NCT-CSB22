print("== Welcome to MindX Restaurant ==")
menu = ['Bun Bo', 'Pho', 'Banh Canh', 'Hu Tieu']
arr =[]
while True:
    order = input('Please choose a dish: ')
    if order in menu:
        if order in arr:
            print('You chose this already. Anything else? (y/n):')
        else: 
            arr.append(order)
            print('Great choice! Anything else? (y/n): ')
    else:
        print("Please choose again")
    yn = input()
    if yn == 'y':
        
        continue
    if yn == 'n':
        print('Well done! Your order:')
        break
for i in arr:
    print(i,"-  ")