def arrayOfProducts(array):
    new_list=[]
    for i in range(0,len(array)):
        print(f"I: {i} ")
        p=1
        for j in range(0,len(array)):
            if i==j:
                continue
            else:
                print(f"{j} values are")
                p=p*array[j]
                print(f"Product is: {p}")
        
        new_list.append(p)


        
        

            

    return new_list





print(arrayOfProducts([5,1,4,2]))