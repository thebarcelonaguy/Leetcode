def threeNumberSum(array, targetSum):
    array.sort()
    list1=[]
    for i,element in enumerate(array): 
        left_pointer=i+1
        right_pointer=len(array)-1
        diff=targetSum-element
        while left_pointer<right_pointer:
            left_element=array[left_pointer]
            right_element=array[right_pointer]
            sum=left_element+right_element
            if sum<diff:
                left_pointer+=1
                
            elif sum>diff:
                right_pointer-=1

            else:
                list2=[]
                list2.extend([left_element,right_element,element])
                list2.sort()
                if list2 not in list1:
                    list1.append(list2)
                left_pointer+=1
                right_pointer+=1


    return list1


array= [12, 3, 1, 2, -6, 5, -8, 6]
target=0
print(threeNumberSum(array,target))