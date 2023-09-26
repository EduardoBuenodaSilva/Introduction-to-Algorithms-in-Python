def merge(L,R):                     #This algorithms is the core of our program it merges
    a = []
    while(R != [] or L != []):      #We loop until one of the list be empty
        
        if(L==[]):                  #If the Left list is empty then, we append to our final list the right list
            a.extend(R)
            return a                 #And stop the loop and the function call
        elif(R==[]):                #If the right list is empty then, we append to our final list the left list
            a.extend(L)
            return a                 #And stop the loop and the function call
        elif(L[0] < R[0]):          #This statement establish that if the L[0] less or equal than R[0] then
            a.append(L[0])          #We append to our final list the L[0]
            L = L[1:]               #This statements is the core of our program it possibilitates we pop the firt
                                    #element by copyng the rest of the list using the index one.
        else:                       #This statements just is true when L[0] is grater than R[0]
            a.append(R[0])          #Im this case we append to our final list the value of R[0]
            R = R[1:]


def merge_sort(alist):
    if len(alist) == 1:
        return alist

    list1 = alist[:len(alist)//2]
    list2 = alist[len(alist)//2:]

    ans1 = merge_sort(list1)
    ans2 = merge_sort(list2)
    return merge(ans1,ans2)



s = merge_sort([3,4,32,5,6,78,2,12,2,4,1,2,3,4,5,6,7,8])
print(s)
