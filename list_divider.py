def merge_sort(my_list):

	# Base Case
    if len(my_list) <= 1:
        print(my_list)
        return my_list
   
    list_1 = my_list[0:len(my_list) // 2]
    list_2 = my_list[len(my_list) // 2:]
    
   	# Induction Step
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)
    
    print(ans_1, ans_2)

x=[]
x.append(merge_sort([0,1,2,3,4,5,6,7,8,9,0,2,3,4,56,7,]))

print(x)
