def sortedSquaredArray(array):
    left_pointer=0
    right_pointer=len(array)-1
    array_final=[0 for _ in array]
    for i in range(len(array_final)-1,-1,-1):
        if (left_pointer==right_pointer):
            array_final[i]=array[left_pointer]**2

            
        elif (abs(array[left_pointer])>abs(array[right_pointer])):
            array_final[i]=array[left_pointer]**2
            left_pointer+=1

        else:
            array_final[i]=array[right_pointer]**2
            right_pointer-=1

    return array_final

print(sortedSquaredArray([-9,-8,7,-1,2,3,4,5,6,7,8]))


    

print(sortedSquaredArray([-9,-8,7,-1,2,3,4,5,6,7,8]))