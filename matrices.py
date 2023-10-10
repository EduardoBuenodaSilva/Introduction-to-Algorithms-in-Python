def line_column(B):
    Matrix = []
    Index = 0
    for i in range(0,len(B[0])):
        Line = []
        for ELine in B:
            Line.append(ELine[Index])
        Matrix.append(Line)
        Index += 1   
    return Matrix

def matrix_multiplier(A,B):
    if len(A[0]) == len(B):
        Bb = line_column(B)
        i = j = 0
        Answer = []
        for Line in A:
            NewLine = []
            for Column in Bb:
                element = 0
                for i in range(len(Column)):
                    element = element + Line[i]*Column[i]
                NewLine.append(element)
            Answer.append(NewLine)
        return Answer


##################################
#Test Generator
"""import random as rd

a = rd.randint(3,5)
b = rd.randint(2,5)
c = rd.randint(3,5)

print(a,b,c)

First_matrix = []
Second_matrix = []

for i in range(a):
    line = []
    for i in range(b):
        line.append(rd.randint(1,20))
    First_matrix.append(line)

for i in range(b):
    line = []
    for i in range(c):
        line.append(rd.randint(1,20))
    Second_matrix.append(line)

for i in First_matrix:
    print(i)

print('\n')
for i in Second_matrix:
    print(i)

print('\n')



answer = matrix_multiplier(First_matrix, Second_matrix)

for i in answer:
    print(i)"""