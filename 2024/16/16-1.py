def h(node):
    return abs(node.x-ex)*abs(node.y-ey)

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.f = 100000000000000
        self.g = 100000000000000
        self.camefrom = None


# with open("test.txt") as f:
with open("data.txt") as f:

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

    start.g = 0
    start.f = h(start)
   
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

        if (c[0],c[1]) == (ex,ey):
            print(current.g)



        for dir in d:
            if lines[cx+dir[0]][cy+dir[1]] != "#":

                neigh = nodes[(cx+dir[0],cy+dir[1])]
                
                tent_g = current.g + 1 + t[abs(d.index(dir)-d.index(cd))]*1000

                if tent_g < neigh.g:

                    neigh.camefrom = current
                    neigh.g = tent_g
                    neigh.f = tent_g + h(neigh)
                    if neigh not in tocheck:
                        tocheck.append((cx+dir[0],cy+dir[1],dir))




    
        

