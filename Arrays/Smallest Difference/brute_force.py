def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    list1=[]
    smallest_diff=float("inf")
    new_diff= float("inf")
    for element_one in arrayOne:
        for element_two in arrayTwo:
            if element_one>element_two:
                new_diff= abs(element_one-(element_two))
            else:
                new_diff= abs(element_two-(element_one))
            if new_diff<smallest_diff:
                smallest_diff=new_diff
                list1=[element_one,element_two]
                
        
    
    return(list1)




arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]


print(smallestDifference(arrayOne,arrayTwo))