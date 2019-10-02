##  4.1-2

array_sub = [100,-2,0,100,-5,-10]
def find_sub_sum(arr):
    max_start = 0
    max_end = len(arr)
    max_sum = 0
    current_sum = 0
    
    for start_index in range(0, len(arr)-1):
        current_sum = (arr[start_index])
        for end_index in range(start_index + 1,len(arr)):
            current_sum += (arr[end_index])
            if current_sum > max_sum:
                max_sum = current_sum
                max_start = start_index
                max_end = end_index
    
            
    print('Max_Sum: ' + str(max_sum))
    print('Start Index: ' + str(max_start))
    print('End Index: ' + str(max_end))

find_sub_sum(array_sub)
