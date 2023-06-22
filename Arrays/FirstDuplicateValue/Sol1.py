def firstDuplicateValue(array):
    min_index=len(array)
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:
                if j<min_index:
                    min_index=j

              
    if min_index==len(array):
        return -1
    else:
        return array[min_index]





print(firstDuplicateValue([2,1,5,2,3,3,4]))
