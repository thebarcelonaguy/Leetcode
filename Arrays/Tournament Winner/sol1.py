def tournamentWinner(competitions, results):
    list1=[]
    for x in competitions:
        for y in x:
            list1.append(y)
    unique_list=list(set(list1))
    hash_map={}
    for x in unique_list:
        hash_map[x]=0
    

    for i in range(0,len(competitions)):
        if results[i]==0:
            hash_map[competitions[i][1]]+=3
        else:
            hash_map[competitions[i][0]]+=3

    
    max_key=max(hash_map,key=hash_map.get)



    return max



competitions=[["HTML","C#"],["C#","Python"],["Python","HTML"]]

results=[0,0,1]

print(tournamentWinner(competitions,results))