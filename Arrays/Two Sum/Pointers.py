from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_pointer=0
        right_pointer=len(nums)-1
        nums_copy=nums.copy()
        nums_copy.sort()

        while(left_pointer<right_pointer):
            sum_value=nums_copy[left_pointer]+nums_copy[right_pointer]
            if target == sum_value:
                left_index=  nums.index(nums_copy[left_pointer])
                right_index= len(nums)-nums[::-1].index(nums_copy[right_pointer])-1
                return [left_index,right_index]
            elif sum_value < target:
                left_pointer+=1
            elif sum_value > target:
                right_pointer-=1 
        
        return []


target=-19
array3=[-10,-1,-18,-19]
x=Solution()
print(x.twoSum(array3,target))    