
def threeNumberSum(nums, targetSum):
    nums.sort()
    triplets=set()
    list1=[]
    for i in range(len(nums)-2): 
        left_pointer=i+1
        right_pointer=len(nums)-1
        while left_pointer<right_pointer:
            left_element=nums[left_pointer]
            right_element=nums[right_pointer]
            sum=left_element+right_element+nums[i]
            if sum<targetSum:
                left_pointer+=1
                
            elif sum>targetSum:
                right_pointer-=1

            else:
                
                triplets.add((nums[i],left_element,right_element))
                left_pointer+=1
                right_pointer-=1

    for x in triplets:
        list1.append(list(x))
        
    return list1


nums= [-1,0,1,2,-1,-4]
target=0
print(threeNumberSum(nums,target))