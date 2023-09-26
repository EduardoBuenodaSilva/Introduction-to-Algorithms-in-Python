# This algorithm adds  two binary numbers based on the truth table created in digital electronics, with the logic of a full adder
# In resume this is a un-limited extend full adder
# inputs: lista and listb, where the only restriction not specified by the program is that they must have the same range
# Output: listc where they have the length of lista or listb incresed by one


def add_bin(lista, listb):          
    i = 0                                               #control variable of loop looking at the lentgh of the inputs and outputs
    listac = [0]                                        #As it is based on full-adder logic it is the carry list and the firts carry number in position 0 is 0
    listc = []                                          #This is the output list that starts empty
    while i <= (len(lista)):                            #As the output result must have an lenth of len(lista)+1 we used <=
        if i == (len(lista)):                           #This block of code must just happen when is equal len(lista)+1, where inside the loop when the test is 0 or 1 the carry will be 0 and when test is 2 or 3 it will be 1
            if test == (0) or test == (1):
                listc.append(0)
            elif test == (2) or  test == (3):
                listc.append(1)
            return listc                                #The loop must end in this step to prevent any kind of list out of range error
        
        test = lista[i] + listb[i] + listac[i]          #Here is the core of the code the sum value in decimal number it will be tested and apropriately will define the values of carry and output in the position of i
        
        if test == 0:
            listc.append(0)
            listac.append(0)
        elif test == 1:
            listc.append(1)
            listac.append(0)
        elif test == 2:
            listc.append(0)
            listac.append(1)
        elif test == 3:
            listc.append(1)
            listac.append(1)
        i+=1                                            #Here the controling loop is being added 


lista = [1,1,1,1]
listb = [1,0,1,1]

print(add_bin(lista, listb))
            
