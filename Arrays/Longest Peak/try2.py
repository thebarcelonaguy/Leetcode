def longestPeak(array):
    list1=[]
    left_pointer=0
    length_peak=0
    for i in range(1,len(array)-1):
        if array[i]>array[i+1] and array[i]>array[i-1]:
            print(f"Tip foound at {array[i]}")
            length_peak=i-left_pointer
            print(f"after subtracting length of peak is {length_peak}")
            left_pointer=i
            for j in range(left_pointer,len(array)-1):
                if array[j]>array[j+1]:
                    print("Yo peak is okay")
                    length_peak+=1
                else:
                    list1.append(length_peak)
                    print(f"Now length is{length_peak}")
                    length_peak=1
                    break
        
    return list1



array=[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
array1=[1,4,10,11,12,23,22,24,25,20,18,19]
array3=[1,3,2]
print(longestPeak(array))