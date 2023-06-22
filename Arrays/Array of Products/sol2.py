def arrayOfProducts(array):
    new_list=[]
    left_list=[]
    right_list=[]
    for x in range(0,len(array)):
        left_list.append(1)
        right_list.append(1)
    p=1
    for i in range(0,len(array)):
        left_list[i]=p
        p=p*array[i]
    q=1
    for j in reversed(range(0,len(array))):
        right_list[j]=q
        q=q*array[j]

        
    for i in range(0,len(array)):
        new_list.append(left_list[i]*right_list[i])
        

            

    return new_list





print(arrayOfProducts([5,1,4,2]))