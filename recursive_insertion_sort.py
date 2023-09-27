
def sort(Array, j):
    key = Array[j]
    while(Array[j-1] > key) and j>0:
        acc = Array[j]
        Array[j] = Array[j-1]
        Array[j-1] = acc
        j= j-1


def insert_sort(Array, p):
    if p+1 < len(Array):
        j = p+1
        sort(Array, j)
        insert_sort(Array, j)
        

a = [100,3,41,52,26,38,57,9,49]
insert_sort(a, 0)
print(a)
    
        
        
