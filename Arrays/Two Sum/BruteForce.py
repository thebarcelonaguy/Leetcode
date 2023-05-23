def twoNumberSum(array, targetSum):
    list1=[]
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if targetSum==array[i]+array[j]:
                list1.append(i)
                list1.append(j)
                return list1
                



array1= [3,5,-4,8,11,1,-1,6]
targetSum=10
array2=[3,2,4]
target=6
array3=[3,3]
print(twoNumberSum(array1,targetSum))        