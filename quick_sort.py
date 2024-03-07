def quick_sort(lst,start,stop):
    i = start
    j = piv = stop
    j-=1
    while i <= j:
        while lst[i] < lst[piv] and i <= j:
            i+=1
        while lst[j] > lst[piv] and i <= j:
            j+=1
        lst[i], lst[j] = lst[j], lst[i]
        i+=1
        j-=1
    return j-1

A = [1, 2, 4, 3, 1, 5, 7, 7]
print(A)
new_split_point = -1
wektor = [-1,len(A)-1]
quick_sort(A,0,len(A)-1)
for x in range(len(A)-1):
    nowy_wektor = [-1,]
    for y in range(len(wektor)-1):
        new_split_point = quick_sort(A, wektor[y]+1, wektor[y+1])
        nowy_wektor.append(new_split_point)
    print(A,wektor)
    nowy_wektor.append(len(A)-1)
    wektor = nowy_wektor
print(A)