def merge(array, p, q, r):
    left = array[p:q]
    right = array[q:r]
    print(left, right)

    top_left , top_right = 0,0
    for k in range(p,r):
        if top_left >= len(left):
            array[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            array[k] = left[top_left]
            top_left = top_left + 1
        elif(left[top_left] < right[top_right]):
            array[k] = left[top_left]
            top_left = top_left+1
        else:
            array[k] = right[top_right]
            top_right = top_right + 1
            
            


def merge_sort(array, p, r):
    if r-p > 1:
        q = (r+p)//2
        merge_sort(array, p, q)
        merge_sort(array, q, r)
        merge(array,p,q,r)
    

a=[9,8,7,6,5,4,3,2,1,0]
b = merge_sort(a,0,len(a))
print(a)
