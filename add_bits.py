A = [1,0,1,1,0,1]
B = [0,1,0,1,1,0]
def add_bits(A,B):
    C = []
    remainder = False
    for index in reversed(range(len(A))):
        print(index)
        sums = A[index] + B[index]
        if remainder: 
            if sums + 1 == 2:
                remainder = True
                C.append(0)
                if(index == 0):
                    C.append(1)
            elif sums + 1 == 3:
                remainder = True
                C.append(0)
                if(index == 0):
                    C.append(1)
            else:
                remainder = False
                C.append(sums)
                if(index == 0):
                    C.append(1)
        else:
            if sums == 2:
                C.append(0)
                remainder = True
            else:
                C.append(sums)
                remainder = False
                
    print(C[::-1])

add_bits(A,B)
