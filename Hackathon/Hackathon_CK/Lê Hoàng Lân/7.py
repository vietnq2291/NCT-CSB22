so = [5, 1, 8, 92, -1, 30]
a = len(so)
print(f"Original list:{so}")
def sort1(so):
    for i in range (0,a-1):
        for j in range (i+1,a):
            if so[j] < so[i]:
                x = so[i]
                so[i] = so[j]
                so[j] = x
    return so
print(f"Sorted list: {sort1(so)}  ")