## 6.5-3

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

# Get index of parent node given child index
def get_parent_index(index):
    if index == 1 or index == 2:
        return 0
    elif(index % 2 != 0):
        return int((index - 1) / 2)
    else:
        return int((index - 2) / 2) 
    
    
## HEAP-MINIMUM
def minimum(arr):
    return arr[0]        
        
## HEAP-EXTRACT-MIN
def extract_min(arr):
    #Make sure that we are starting with a min heap
    build_min_heap(arr)
    
    n = len(arr)
 
    #Make sure the length of the heap is greater than 1
    if n < 1:
        exit()
        
    min_value = arr[0] # min value to return
    
    #replace first value (to be removed)
    arr[0] = arr[n-1] 
    
    #remove last value of array
    arr.pop()
    
    new_len = len(arr)
    
    #return array to heap state
    heapify(arr, new_len, 0)
    return min_value

## HEAP-DECREASE-KEY
    
def decrease_key(arr, i, key):
    if key > arr[i]:
        exit()
        
    arr[i] = key
    
    # Check if parent is greater than child
    # if it is then swap child and parent and repeat loop
    # Continue loop untill parent of the decreased key is smaller than the decreased key
    while i > 0 and arr[get_parent_index(i)] > arr[i]:
        print(arr)
        arr[i], arr[get_parent_index(i)] = arr[get_parent_index(i)], arr[i]
        i = get_parent_index(i)
        
## MIN-HEAP-INSERT
def insert(arr, value):
    n = len(arr)
    arr.append(float('inf'))

    #Place inserted value into correct place
    decrease_key(arr, n - 1, value)
    
    
