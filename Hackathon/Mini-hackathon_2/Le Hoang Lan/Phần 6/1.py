dt = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
pp = [247100,333300,266800,420900,318000]
s = [9.224,43.35,12.04,9.96,10.09]
d = []
for x in pp:
    d.append(int(x)/s[pp.index(x)])
for y in dt:
    print(f'{y}: {d[dt.index(y)]}')