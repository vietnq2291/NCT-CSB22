dt = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
pp = [247100,333300,266800,420900,318000]
s = [9.224,43.35,12.04,9.96,10.09]
sum = 0
for x in pp:
    a = int(x)/s[pp.index(x)]
    sum +=a
av = sum/5
print('Average population density: ',av)
