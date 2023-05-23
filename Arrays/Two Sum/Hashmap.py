
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,num in enumerate(nums):
            expected_diff=target-num
            if expected_diff in dict1:
                return [i,dict1[expected_diff]]
            else:
                dict1[num]=i

        return []


target=9
array3=[2,7,11,15]
x=Solution()
print(x.twoSum(array3,target))        