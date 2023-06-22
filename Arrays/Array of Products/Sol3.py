def arrayOfProducts(array):
    new_list=[]
    for x in range(0,len(array)):
        new_list.append(1)
    p=1
    for i in range(0,len(array)):
        new_list[i]=p
        p=p*array[i]

    q=1
    for j in reversed(range(0,len(array))):
        new_list[j]*=q
        q=q*array[j]

        
            

    return new_list





print(arrayOfProducts([5,1,4,2]))