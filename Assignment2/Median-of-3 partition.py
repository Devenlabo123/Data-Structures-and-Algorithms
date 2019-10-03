#########    Median-of-3 partition    ##########

import random
import statistics


def quicksort(arr, start, end):
    if start < end:
        q = partition(arr, start, end)
        quicksort(arr, start, q - 1)
        quicksort(arr, q + 1, end)

    
    
def partition(arr, start, end):
    rand_values = [random.choice(arr[start:end + 1]), random.choice(arr[start:end + 1]), random.choice(arr[start:end + 1])]
    pivot_value = statistics.median(rand_values)
    pivot_index = arr.index(pivot_value)
    
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    
    
    i = start - 1
    
    for j in range(start, end):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1

arr = [12, 7, 15, 3, 7, 8, 19, 2] 
quicksort(arr, 0, len(arr) - 1) 
for i in range(len(arr)): 
    print (str(arr[i]) + ' ')
