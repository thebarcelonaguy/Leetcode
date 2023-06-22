def firstDuplicateValue(array):
    set1=set()
    for i in array:
        if i not in set1:
            set1.add(i)
        else:
            return i
    
    return -1





print(firstDuplicateValue([2,1,5,3,3,2,4]))
