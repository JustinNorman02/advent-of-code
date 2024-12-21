def h(node):
    return abs(node.x-ex)*abs(node.y-ey)

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.f = [100000000000000,100000000000000,100000000000000,100000000000000]
        self.g = [100000000000000,100000000000000,100000000000000,100000000000000]
        self.camefrom = []


def counttiles(node):
    to_search = [node]
    seen = []

    while to_search:
        node = to_search.pop(0)
        seen.append(node)
        m = min(node.g)

        if m == 0:
            continue

        idx = [d[i] for i, value in enumerate(node.g) if value == m]

        for x,y in idx:

            to_search.append(nodes[node.x-x,node.y-y])

    return len(seen)


    
def printseen(board,seen):

    for node in seen:
        board[node.x][node.y] = 'O'

    for line in board:
        print("".join(line))


checked = []

with open("test.txt") as f:
# with open("data.txt") as f:

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

    nodes = {(i,j):Node(i,j) for j in range(len(lines[1])) for i in range(len(lines)) if lines[i][j] != '#'}
    

    d= [(-1,0),(0,1),(1,0),(0,-1)]

    start = nodes[(sx,sy)]

    start.g = [0,0,0,0]
    start.f = [h(start),h(start),h(start),h(start)]
   
    t = [0,1,2,1]

    tocheck = [(sx,sy, d[1])]

    cd = d[1]

    while tocheck:
        tocheck = sorted(tocheck, key=lambda idx: nodes[(idx[0],idx[1])].f)

        c = tocheck[0]

        tocheck.pop(0)
        current = nodes[(c[0],c[1])]
        
        cx,cy = c[0], c[1]
        cd = c[2]



        for i, dir in enumerate(d):
            if lines[cx+dir[0]][cy+dir[1]] != "#":

                neigh = nodes[(cx+dir[0],cy+dir[1])]
                
                tent_g = current.g[d.index(cd)] + 1 + t[abs(d.index(dir)-d.index(cd))]*1000

                if tent_g < neigh.g[i]:

                    neigh.camefrom = current
                    neigh.g[i] = tent_g
                    neigh.f[i] = tent_g + h(neigh)
                    tocheck.append((cx+dir[0],cy+dir[1],dir))


print(nodes[(ex,ey)].g)


print(counttiles(nodes[(ex,ey)]))
    
        

