def isValidSubsequence(array, sequence):
    array_index=0
    sequence_index=0
    while(array_index<len(array)):
        if array[array_index]==sequence[sequence_index]:
            sequence_index+=1
        array_index+=1
        if len(sequence) == sequence_index:
            break
    return len(sequence) == sequence_index





    




array= [5, 1, 22, 25, 6, -1, 8, 10]
sequence= [1,6,23,-1,10]
print(isValidSubsequence(array,sequence))