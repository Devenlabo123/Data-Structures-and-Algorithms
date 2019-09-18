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
        
arrs = [7,11,12,14,15,7,8,1] 
size = len(arrs)
# Build a maxheap
for i in range(size, -1, -1):
    heapify(arrs, size, i)

print(arrs)
