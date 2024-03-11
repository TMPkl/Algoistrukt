def shellSort(array, n):
    interval = n // 2

    while interval > 0:
        i = interval
        while i < n:
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
            i += 1
        interval //= 2
    return array

A = [3, 2, 4, 1]