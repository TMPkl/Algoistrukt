def mergeSort(lst):
    counter = 0
    if len(lst) > 1:

        pivot = len(lst) // 2

        L = lst[:pivot]
        R = lst[pivot:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        counter+=1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
            
    return lst

A = [2,
6,
46,
35,
8,
3,]

print(mergeSort(A))