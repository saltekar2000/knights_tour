import numpy as np

BOARDSIZE_X = 6
BOARDSIZE_Y = 6
BOARDSIZE = (BOARDSIZE_X,BOARDSIZE_Y)

def knights_tour( i, j, visited = np.zeros(BOARDSIZE, dtype = bool), tour = np.zeros(BOARDSIZE, dtype = int), depth = 0 ):
    #print depth
    if i < 0 or j < 0 or i >= BOARDSIZE_X or j >= BOARDSIZE_Y or visited[i][j]:
        return
    depth += 1
    visited[i][j] = True
    tour[i][j] = depth
    if depth == BOARDSIZE_X*BOARDSIZE_Y:
        print tour
        return True
    knights_tour(i+2,j+1,visited,tour,depth)
    knights_tour(i+2,j-1,visited,tour,depth)
    knights_tour(i-2,j+1,visited,tour,depth)
    knights_tour(i-2,j-1,visited,tour,depth)
    knights_tour(i+1,j+2,visited,tour,depth)
    knights_tour(i-1,j+2,visited,tour,depth)
    knights_tour(i+1,j-2,visited,tour,depth)
    knights_tour(i-1,j-2,visited,tour,depth)
    visited[i][j] = False
    tour[i][j] = 0
    depth -= 1
    return False

knights_tour(2,2)



    
    
