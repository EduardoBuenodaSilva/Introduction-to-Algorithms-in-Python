#Algorithm for insertion sort

# This algorithms works by changing the position
# of the itens in a sequence value if it is grater
# less than the iten been compared

def insertionsort(Itens, order):
    a = len(Itens)

    for k in Itens:                             #States that the following statements need to be done for all itens in the list
        i = a-1                                 #This statement garantees that the counting for the list will start by the least item
        while i>0:                              #The inner cicle just ends when it is in the first item
            if order == 'd':                    #This will sort the list in the decrease order
                if Itens[i-1] > Itens[i]:       #This statemente looks if the item in position is grater than the item in the position i-1, the following statements make sure that if this is true a change of values will happen
                    Accumulator = Itens[i-1]    #As the first value to be changed in the sort algorithm is the item in position i-1 than, we retain this value in a accumlator variable
                    Itens[i-1] = Itens[i]       #Then we can replace the value of item i-1 by the grater value that is item in position i
                    Itens[i] = Accumulator      #To make the change complete we replace the value of the item i by the accumlator value
                else:
                    break
            if order == 'i':                    #In this block of code the logic is exacly the same, the only difference is that ir organizes in increasing order
                if Itens[i-1] < Itens[i]:
                    Accumulator = Itens[i-1]
                    Itens[i-1] = Itens[i]
                    Itens[i] = Accumulator
            i -=1                               #This guarantees that the while loop os controled 

    return Itens


L = [31,41,59,26,41,58]
print(insertionsort(L,'i'))
print(insertionsort(L,'d'))

    
        
                
