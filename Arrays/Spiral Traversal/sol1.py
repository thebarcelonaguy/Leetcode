def spiralTraverse(array):
    final_list=[]
    first_row=0
    first_col=0
    last_row=len(array)-1
    last_col=len(array[0])-1
    while(first_row<=last_row and first_col<=last_col):
        for col in range(first_col,last_col+1):
            final_list.append(array[first_row][col])

        for row in range(first_row+1,last_row+1):
            final_list.append(array[row][last_col])

        for col in reversed(range(first_col,last_col)):
            if first_row==last_row:
                break
            final_list.append(array[last_row][col])

        for row in reversed(range(first_row+1,last_row)):
            if last_col==first_col:
                break
            final_list.append(array[row][first_col])


        first_row+=1
        last_row-=1
        first_col+=1
        last_col-=1
    return final_list




array=[[1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

print(spiralTraverse(array))