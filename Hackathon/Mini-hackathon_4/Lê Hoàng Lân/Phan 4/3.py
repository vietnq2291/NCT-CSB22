gcomp = {
    'HP':600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400
}
comp = {
    'HP':20, 'DELL': 50, 'MACBOOK': 12, 'ASUS': 30
}
lap = input("Input a brand: ")
sl = int(input("Input amountto buy: "))
g = comp[lap]
tt = sl*g
print("Total price: ",tt)
comp[lap] = comp[lap] - sl
for i in comp:
    print(f"- {i}: {comp.get(i)}")