def longestPeak(array):
    max_length=0
    for i in range(1,len(array)-1):
        if array[i]>array[i-1] and array[i]>array[i+1]:
            print(f"Peak is {array[i]}")
            left_pointer=i-2
            right_pointer=i+2
            while(left_pointer>=0 and array[left_pointer]<array[left_pointer+1]):
                    print("LEFT COMAPRSION")
                    print(f"was comparing {array[left_pointer-1]} and {array[left_pointer]}")
                    left_pointer-=1
            while(right_pointer<len(array) and  array[right_pointer-1]>array[right_pointer]):
                    print("RIGHT")
                    print(f"was comparing {array[right_pointer]} and {array[right_pointer-1]}")
                    right_pointer+=1
            print(f"final left: {left_pointer} and right: {right_pointer}")       
            curr_length=right_pointer-left_pointer-1
            print(curr_length)
            if curr_length>max_length:
                  max_length=curr_length

    return max_length


array=[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
array1=[1,4,10,11,12,23,22,24,25,20,18,19]
array2=[1,2,3,4,5,1]
print(longestPeak(array2))