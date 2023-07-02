print("Available products:")
comp = {
    'HP':20, 'DELL': 50, 'MACBOOK': 12, 'ASUS': 30, 'TOSHIBA':10
}
comp['DELL'] = 60
comp['MACBOOK'] = 2
for i in comp:
    print(f"- {i}: {comp.get(i)}")