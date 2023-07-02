gcomp = {
    'HP':600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400
}
comp = {
    'HP':20, 'DELL': 50, 'MACBOOK': 12, 'ASUS': 30
}
for i in gcomp:
    a = gcomp[i]*comp[i]
    print(f"-{i}: {a}")