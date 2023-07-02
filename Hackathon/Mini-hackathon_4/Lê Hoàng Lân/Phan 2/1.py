print("Available products:")
comp = {
    'HP':20, 'DELL': 50, 'MACBOOK': 12, 'ASUS': 30
}
comp['TOSHIBA'] = 10
for i in comp:
    print(f"- {i}: {comp.get(i)}")