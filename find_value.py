list_test = [4,3,345,6,5,2,7,8,7,45,6,2,34,13]


# 2.1-3
def find_v(v,A):
    found = False
    
    for i in A:
        if i == v:
            print(i)
            found = True
            break
    
    if found != True:
        print('Nil')
        
find_v(13,list_test)
