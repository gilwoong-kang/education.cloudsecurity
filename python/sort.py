def selection_sort(l:list):
    for i in range(len(l)):
        idx = l.index(min(l[i:]))
        dummy = l[i]
        l[i] = l[idx]
        l[idx] = dummy
    return l


l = [6,16,3,25,2,8,1]
print(selection_sort(l))