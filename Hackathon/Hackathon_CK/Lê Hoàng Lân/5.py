comp = {
    'Iphone12':28000000, 'Samsung N10': 16000000, 'Oppo 93': 7500000, 'Vsmart': 7400000, 'Vivo':4200000
}

input = input("Input a brand: ")
n = comp[input]
print(f"Price of {input}: {n}")