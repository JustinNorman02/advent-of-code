def printseen(board,seen):

    for node in seen:
        board[node.x][node.y] = 'O'

    for line in board:
        print("".join(line))

def dfs(x,y,path):
    global bestpathscore
    d= [(-1,0),(0,1),(1,0),(0,-1)]

    for d2 in d:
        nx, ny = d2[0]+x, d2[1]+y

        if lines[nx][ny] == 'E':
            if scorepath(path) <= bestpathscore:
                bestpathscore = scorepath(path)
                paths.append(path)

        if lines[nx][ny] != '#':
            if (nx,ny) not in path:
                tpath = path
                tpath.append((nx,ny))
                if scorepath(tpath) <= bestpathscore:
                    dfs(nx,ny, tpath)
        

def scorepath(path):

    score = 1
    d= [(-1,0),(0,1),(1,0),(0,-1)]  
    current = path[0]
    path.pop(0)
    cd = d[0]
    turn = [0,1,2,1]
    

    while path:
        next = path[0]
        path.pop(0)
        score += 1

        dir = (next[0]-current[0], next[1]-current[1])

        score += turn[abs(d.index(dir)-d.index(cd))]*1000

        current = next
        cd = dir
    
    return score





with open("test.txt") as f:
# with open("data.txt") as f:

    global bestpathscore 
    bestpathscore = 100000000

    lines = f.read().split("\n")

    sx,sy,ex,ey = 0,0,0,0

    for i in range(len(lines)):
       lines[i] = list(lines[i])

       if 'S' in lines[i]:
           sx = i
           sy = lines[i].index('S')
           
       if 'E' in lines[i]:
           ex = i
           ey = lines[i].index('E')

    paths = []

    dfs(sx,sy, [(sx,sy)])
    
    d= [(-1,0),(0,1),(1,0),(0,-1)]

    tiles = []

    winning_score = 0

    for path in paths:
        score = scorepath(path)

        if score > winning_score:
            tiles = path
            winning_score = score
        
        if score == winning_score:
            for p in path:
                if p not in tiles:
                    tiles.append(p)
        
    
    print(winning_score)
    print(len(tiles))




    




    
        

