def isMonotonic(nums):
    isNonDecreasing=True
    isNonIncreasing=True
    for i in range(1,len(nums)):
        if nums[i]<nums[i+1]:
            isNonDecreasing=False
        if nums[i]>nums[i+1]:
            isNonIncreasing=False
        

    
    return isNonDecreasing or isNonIncreasing




nums=[-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
arraisNonIncreasing1=[1,2,3,3,4,6,9,10,23,89]
fail=[-1, -5, -10, -1100, -900, -1101, -1102, -9001]

print(isMonotonic(nums))
print(isMonotonic(fail))
# print(isMonotonic(arraisNonIncreasing1))