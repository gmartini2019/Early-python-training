from collections import defaultdict

def has_euler_path(g):
    gotIt = False
    oddEdges = 0

    numberOfEdges = [0 for x in range(len(g[0]))]
    for i in range(len(g[0])):
        for j in range(len(g[1])):
            if(g[1][i][0] == g[0][j]):
                numberOfEdges[j]+=1
                for k in range(len(g[0])):
                    if(g[1][i][1] == g[0][k]):
                        numberOfEdges[k]+=1
                        
    for i in range(len(numberOfEdges)):
        if numberOfEdges[i] !=0:
            if numberOfEdges[i]%2 != 0:
                oddEdges += 1
    
    if oddEdges == 2:
        gotIt = True
    
    return gotIt


def list_of_edges(a):

    listOfAdjacents = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]== 1:
                           listOfAdjacents[i].append(j)
    return listOfAdjacents

a =[[0,1,1,1],[1,0,1,0],[1,1,0,0],[1,0,0,0]]  
print(list_of_edges(a))





            

