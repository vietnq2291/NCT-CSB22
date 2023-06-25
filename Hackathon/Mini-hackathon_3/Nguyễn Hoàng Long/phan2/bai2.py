def xap_xep_list(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range (i+1, n):
            if lst[i] > lst[j]:
                lst[j],lst[i] = lst[i],lst[j]

lst = [5,1,8,92,-1,30]
print("Danh sách ban đầu:")
print(*lst,sep=' ')
xap_xep_list(lst)
print("Danh sách đã được sắp xếp:")
print(*lst,sep=' ')
