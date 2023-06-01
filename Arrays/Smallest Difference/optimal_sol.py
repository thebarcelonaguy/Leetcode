def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointer_One=0
    pointer_Two=0
    small_diff=float("inf")
    new_diff=float("inf")
    list1=[]
    while(pointer_One<len(arrayOne) and pointer_Two<len(arrayTwo)):
        element1=arrayOne[pointer_One]
        element2=arrayTwo[pointer_Two]
        if element1==element2:
            return [element1,element2]

        elif element1 > element2:
            new_diff=element1-element2
            pointer_Two+=1
        else:
            new_diff=element2-element1
            pointer_One+=1
        
        if small_diff>new_diff:
            small_diff=new_diff
            list1=[element1,element2]


    return list1


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]


print(smallestDifference(arrayOne,arrayTwo))