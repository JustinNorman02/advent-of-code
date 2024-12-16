def atpush(x,y,dx,dy):
    if wh[x][y] == '#':
        return False
    
    elif wh[x][y] == '.':
        return True
    
    elif wh[x][y] == 'O':
        res = atpush(x+dx,y+dy,dx,dy)

        if res:
            wh[x][y] = "."
            wh[(x+dx)][(y+dy)] = "O"
            return res

        else:
            return res

    else:
        raise RuntimeError
    
def find_indices(matrix, target):
    indices = []
    for i, row in enumerate(matrix):  # Iterate over rows
        for j, element in enumerate(row):  # Iterate over elements in each row
            if element == target:
                indices.append((i, j))  # Append the indices (row, column)
    return indices

def print_board(board):
    for line in board:
        print("".join(line))

    print()

with open('data.txt') as f:

    wh, ins = f.read().split("\n\n")

    wh = wh.split('\n')

    for i in range(len(wh)):
        wh[i] = list(wh[i])

    ins = list(ins.replace('\n',''))

    for i in range(len(wh)):
        for j in range(len(wh[0])):
            if wh[i][j] == "@":
                break

        if wh[i][j] == "@":
            break

    rx, ry = i, j

    dir = {'^':[-1,0], ">":[0,1], "<":[0,-1], "v":[1,0]}

    for i in ins:
        dx,dy = dir[i]
        nx,ny = rx+dx, ry+dy

        loc = wh[nx][ny]

        if loc == '.':
            wh[nx][ny] = '@'
            wh[rx][ry] = '.'
            rx,ry = nx,ny
            

        elif loc == 'O':
            res = atpush(nx,ny,dx,dy)

            if res:
                wh[nx][ny] = '@'
                wh[rx][ry] = '.'
                rx,ry = nx,ny


        elif loc == "#":
            pass

        else:
            raise RuntimeError
        
        # print_board(wh)
        

    boxes = find_indices(wh, 'O')

    ans = 0

    for x,y in boxes:
        ans += 100*x+y

    print(ans)


     
                                             
