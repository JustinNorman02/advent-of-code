import copy

dir = [[1,0],[-1,0],[0,1],[0,-1]]


def score(board, i,j, seen=[]):
    current = int(board[i][j])

    if current == 9 and [i,j] not in seen:
        seen.append([i,j])
        return seen
    
    to_search = []

    for d in dir:
        x,y = i + d[0], j + d[1]

        if 0 <= x < len(board) and 0 <= y < len(board[0]):

            if board[x][y] == '.':
                pass

            elif int(board[x][y]) == current + 1:
                to_search.append([x,y])

    
    if not to_search:
        return seen
    
    
    for x,y in to_search:
        for entry in score(board,x,y,seen):
            if entry not in seen:
                seen.append(entry)
    
    return seen






with open("data.txt") as f:
    board = f.read().split("\n")

    for i in range(len(board)):
        board[i] = list(board[i])

    indices = [(i, j) for i, row in enumerate(board) for j, x in enumerate(row) if x == "0"]

    print(indices)

    ans = []

    for i,j in indices:
        s = len(score(board,i,j, []))
        print(str(i)+","+str(j)+ ' '+ str(s))
        ans.append(s)

    print(sum(ans))
