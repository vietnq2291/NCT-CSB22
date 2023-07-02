comp = {
    'HP':20, 'DELL': 50, 'MACBOOK': 12, 'ASUS': 30, 'TOSHIBA':10
}
lap = input("Input a brand: ")
sl = input("Input amount: ")
comp[lap] = sl
print("Available products:")
for i in comp:
    print(f"- {i}: {comp.get(i)}")