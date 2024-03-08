def quick_sort(lst,start,stop):
    if len(lst) == 1:
        return 
    i = start
    j = piv = stop
    j-=1
    while i <= j:
        while lst[i] < lst[piv] and i <= j and lst[j] > lst[piv]:
            i+=1            ############################ tutaj muszę to robic po kroku a nie max i min j 
            if lst[i] < lst[piv] and lst[j] > lst[piv]:
                break
            j+=1
        lst[i], lst[j] = lst[j], lst[i]
        i+=1
        j-=1
    if j-1 <= start:
        if start+1 <= stop:
            return start+1
        else:
            return stop-1
    
    return j-1

A = [1, 8, 3, 4 , 5, 1, 6, 2]
print(A)
new_split_point = len(A)-1
wektor = [-1,len(A)-1]
quick_sort(A,0,len(A)-1)
for x in range(len(A)-1):
    nowy_wektor = [-1,]
    for y in range(len(wektor)-1):
        new_split_point = quick_sort(A, wektor[y]+1, wektor[y+1])
        nowy_wektor.append(new_split_point)
    print(A,wektor)
    nowy_wektor.append(len(A)-1)
    nowy_wektor.sort()
    wektor = nowy_wektor
print(A)