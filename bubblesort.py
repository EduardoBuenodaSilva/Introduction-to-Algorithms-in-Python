import random as rd

def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if array[j] < array[j-1]:
                acc = array[j-1]
                array[j-1] = array[j]
                array[j] = acc

array = rd.sample(range(0,9), 9)
print(array)
bubblesort(array)
print(array)
