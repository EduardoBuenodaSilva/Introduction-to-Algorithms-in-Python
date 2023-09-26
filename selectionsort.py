
def selectionsort(alist):               #The selection sort is an algorithm that find the smallest element and exchnge it with the element in the position it is comparing
    for k in range(len(alist)):             #This finds the index of the element to be compared
        for i in range(len(alist)):         #This loop searchs the smallest element remaining in the list[k to len(a)]
            if alist[k]< alist[i]:              #This statement guarantees where the exchange will be made
                b = alist[k]
                alist[k] = alist[i]
                alist[i] = b

    return alist


print(selectionsort([1,2,6,8,4,5,9,3]))


