def atpush(x,y,y2,dx,dy):

    if dx != 0: #verticle

        if wh[x][y] == '#' or wh[x][y2] == '#':
            return False
        
        elif wh[x][y] == '.' and wh[x][y2] == '.':
            return True
        
        
        elif wh[x][y] == '[' and wh[x][y2] == ']':
            res = atpush(x+dx,y+dy,y2+dy,dx,dy)

            if res:
                wh[x][y], wh[x][y2] = ".", '.'
                wh[(x+dx)][(y+dy)], wh[(x+dx)][(y2+dy)]  = "[","]"
                return res

            else:
                return res
            
        elif wh[x][y] == ']' and wh[x][y2] == '[':
            res1 = testpush(x,y-1,y,dx,dy)
            res2 = testpush(x,y2,y2+1,dx,dy)

            if res1 and res2:
                res1 = atpush(x,y-1,y,dx,dy)
                res2 = atpush(x,y2,y2+1,dx,dy)

                if res1 and res2:
                    wh[x][y], wh[x][y2], wh[x][y2+1], wh[x][y-1]  = ".", '.', '.','.'
                    wh[(x+dx)][(y-1+dy)], wh[(x+dx)][(y+dy)]  = "[","]"
                    wh[(x+dx)][(y2+dy)], wh[(x+dx)][(y2+1+dy)]  = "[","]"
                    return True
                    
                else: #Can push but push failing
                    raise RuntimeError
                
            else: #Cannot push dual boxes
                return False

        elif wh[x][y] == ']':
            res = atpush(x,y-1,y,dx,dy)
            return res

        elif wh[x][y2] == '[':
            res = atpush(x,y2,y2+1,dx,dy)
            return res
            

        else: #Cannot push
            return False
        
    elif dy != 0: #horizontal

        if dy == 1: #if pushing right check for box to the right
            if wh[x][y] == '#':
                return False
            
            elif wh[x][y] == '.':
                return True
            
            elif wh[x][y] == '[' and wh[x][y2] == ']':
                res = atpush(x+dx,y2+dy,y2+2*dy,dx,dy)
                if res:
                    wh[x][y] = "."
                    wh[(x+dx)][(y+dy)], wh[(x+dx)][(y2+dy)]  = "[","]"
                    return res

                else:
                    return res

                
            else: #Next item isnt in valid list of items
                raise RuntimeError

        if dy == -1: #if pushing right check for box to the right
            if wh[x][y2] == '#':
                return False
            
            elif wh[x][y2] == '.':
                return True
            
            elif wh[x][y] == '[' and wh[x][y2] == ']':
                
                res = atpush(x+dx,y+2*dy,y+dy,dx,dy)
                if res:
                    wh[x][y2] = "."
                    wh[(x+dx)][(y+dy)], wh[(x+dx)][(y2+dy)]  = "[","]"
                    return res
                else:
                    return res

            else: #Next item isnt in valid list of items
                raise RuntimeError 


        else: #if not left or right then why are you checking horizontal
            raise RuntimeError


        
        
    else: #Not moving in a defined direction
        raise RuntimeError
    

def testpush(x,y,y2,dx,dy):
     if dx != 0: #verticle

        if wh[x][y] == '#' or wh[x][y2] == '#':
            return False
        
        elif wh[x][y] == '.' and wh[x][y2] == '.':
            return True
        
        elif wh[x][y] == '[' and wh[x][y2] == ']':
            res = testpush(x+dx,y+dy,y2+dy,dx,dy)

            return res
            
        elif wh[x][y] == ']' and wh[x][y2] == '[':
            res1 = testpush(x,y-1,y,dx,dy)
            res2 = testpush(x,y2,y2+1,dx,dy)

            if res1 and res2:
                return True
            else:
                return False

        elif wh[x][y] == ']':
            return testpush(x,y-1,y,dx,dy)

        elif wh[x][y2] == '[':
            return testpush(x,y2,y2+1,dx,dy)

        else:
            return False
    
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

    wh2 =[]

    for i in range(len(wh)):
        wh2.append([])
        for j in range(len(wh[0])):
            if wh[i][j] == "#":
                wh2[i].append("#")
                wh2[i].append("#")

            elif wh[i][j] == "O":
                wh2[i].append("[")
                wh2[i].append("]")


            elif wh[i][j] == ".":
                wh2[i].append(".")
                wh2[i].append(".")

            elif wh[i][j] == "@":
                wh2[i].append("@")
                wh2[i].append(".")

            else:
                raise RuntimeError
            
    wh = wh2

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
        # print("Move:", i)
        # print_board(wh)

        dx,dy = dir[i]
        nx,ny = rx+dx, ry+dy

        loc = wh[nx][ny]

        if loc == '.':
            wh[nx][ny] = '@'
            wh[rx][ry] = '.'
            rx,ry = nx,ny
            

        elif loc == '[':
            res = atpush(nx,ny,ny+1,dx,dy)

            if res:
                wh[nx][ny] = '@'
                wh[rx][ry] = '.'
                rx,ry = nx,ny

        elif loc == "]":
            res = atpush(nx,ny-1,ny,dx,dy)

            if res:
                wh[nx][ny] = '@'
                wh[rx][ry] = '.'
                rx,ry = nx,ny


        elif loc == "#":
            pass

        else:
            raise RuntimeError
        
        
    print_board(wh)


    ans = 0

    boxes = find_indices(wh, '[')

    for x,y in boxes:
        ans += x*100+y

    print(ans)


     
                                             
