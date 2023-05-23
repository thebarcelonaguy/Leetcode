def tournamentWinner(competitions, results):
    currentBestTeam=""
    hash_map={currentBestTeam:0}

    for index,element in enumerate(competitions):
        home_team,away_team=element

 
        winningTeam= home_team if results[index]==1 else away_team
        
        updatescores(winningTeam,hash_map)


    
        if hash_map[winningTeam]>hash_map[currentBestTeam]:
            currentBestTeam=winningTeam

    return currentBestTeam



def updatescores(team,hash_map):
    if team not in hash_map:
        hash_map[team]=3
    else:
        hash_map[team]+=3


competitions=["HTML", "Java"],["Java", "Python"],["Python", "HTML"]

results=[0,1,1]

print(tournamentWinner(competitions,results))