comp = {
    'HP':600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400
}
lap = input("Input a brand: ")
sl = int(input("Input amountto buy: "))
g = comp[lap]
tt = sl*g
print("Total price: ",tt)