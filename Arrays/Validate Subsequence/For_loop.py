def isValidSubsequence(array, sequence):
    array_index=0
    sequence_index=0
    for element in array:
        if sequence_index==len(sequence):
            break
        if element==sequence[sequence_index]:
            sequence_index+=1

    return sequence_index==len(sequence)