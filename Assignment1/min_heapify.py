## 6.2-2
  
# i --> Parent index 
# n --> size of heap 
def heapify(arr, n, i): 
    largest = i  # root node index
    l = 2 * i + 1  # left node index
    r = 2 * i + 2  # right node index
  
    # See if left child of root exists and is less than root 
    if l < n and arr[i] > arr[l]:
        largest = l 
  
    # See if right child of root exists and is less than root 
    if r < n and arr[largest] > arr[r]: 
        largest = r 
  
    #Check if index of largest node has changed
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # Swap root and child's place in array
  
        # Heapify the root. 
        heapify(arr, n, largest) 


def build_min_heap(arr):
    heap_size = len(arr)
    for i in range(heap_size, -1, -1): 
        heapify(arr, heap_size, i) 


arr = [7, 11, 12, 14, 15, 7, 8, 1]
build_min_heap(arr)
print(arr)

#test for random set of numbers non power of two
arr = [8, 5, 4, 33, 5, 66, 8, 102, 130, 123, 64, 705, 124]
build_min_heap(arr)
print(arr)

#test for reverse sorted non power of two
arr = [1, 2, 3, 4, 5, 6, 7]
build_min_heap(arr)
print(arr)

#test for pre sorted non power of two
arr = [7, 6, 5, 4, 3, 2, 1]
build_min_heap(arr)
print(arr)
