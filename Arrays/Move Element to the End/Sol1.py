def moveElementToEnd(array, toMove):
    left_pointer=0
    right_pointer=len(array)-1
    swap_number=0
    while(left_pointer<right_pointer):
        left_element=array[left_pointer]
        right_element=array[right_pointer]
                

        if(right_element==toMove):
            right_pointer-=1
            continue
        
        if left_element==toMove:
            swap_number=array[right_pointer]
            array[right_pointer]=array[left_pointer]
            array[left_pointer]=swap_number
        left_pointer+=1
 
    return array


array=[2, 4, 2, 5, 6, 2, 2]
toMove=2
print(moveElementToEnd(array,toMove))