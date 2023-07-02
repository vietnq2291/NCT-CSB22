comp = {
    'HP':600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400
}

input = input("Input a brand: ")
n = comp[input]
print(f"Price of {input}: {n}")