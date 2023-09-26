def recursive_search(alist, value):
        if len(alist) == 1:
                if alist[0] == value:
                        return True
                return False

        Answer1 = recursive_search(alist[:len(alist)//2], value)
        Answer2 = recursive_search(alist[len(alist)//2:], value)
        return Answer1 or Answer2

        
b = [1,2,3,4,44,5,66,7,1,2,35,6]
s = recursive_search(b, 35)
print(s)
