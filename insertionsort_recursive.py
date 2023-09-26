#This function called  insertion expects a list and a index, the list is expected to be already sorted
#The index will always be corresponding of the last item in the list A. With this index we find our item
#And create a key, this key is another piece of memory because, we will place this value in the list A
#where the adjacents elements are less or equal than the item, or grater or equal than item

def insertion(A, j):                        #This function expects a already sorted list and a index
    key = A[j]                              #Creates a key that will sort in our list
    while key < A[j-1] and j>0:             #We look where the key will be placed and stops in the first item
        acc = A[j-1]                        #we are making a changing of position using a accmulator
        A[j-1] = key                        #if the key is less than the a[j-1] we change its value with key
        A[j] = acc                          #here we complete the change placing in memory the value of acc into A[j]
        j = j-1                             #This garantees the loop control

#Take note that the value of key does not change inside the while loop


#This functions garantees the recursion tree for every item in the list, the objetctive of this tree is simple
#create a structure where we reduce the value of j-1 creating no reference in menory for the sub-array already sorted
#A[0...j-1] the bottom of this structure is A[0] that has just one element already sorted
def insertion_sort(A, j):
    if j>0:                                 #We are going to go inside the tree structure while index is grater than 0
        insertion_sort(A,j-1)               #Here is where the recursion occurs
        insertion(A,j)                      #Here is where the insertion of the element in the A list happens
    

a = [3,4,5,6,7,2121212,2221,11,2,7,8,9,0,0,4,43,3,7]
insertion_sort(a, len(a)-1)
print(a)
