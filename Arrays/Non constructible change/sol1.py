def nonConstructibleChange(coins):

    change=1
    coins.sort()
    for i in coins:
        if i<change+1:
            change=change+i
            print(change)
        else:
            return change  
        
    return change


coins=[1, 1, 1, 1, 1]
print(nonConstructibleChange(coins))
