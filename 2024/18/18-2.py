def print_map(grid):
    for line in grid:
        print("".join(line))



# with open("test.txt") as f:
with open("data.txt") as f:

    lines = f.read().split("\n")

    for i in range(len(lines)):
       lines[i] = [int(j) for j in lines[i].split(',')]


    n,m = 71,71

    sx,sy = 0,0
    ex,ey = n-1,m-1


    l = m*n

    while l >= 0:
        print(l)

        grid = [['.' for i in range(n)] for j in range(m)]

        search = []
        
        for i in range(m):
            for j in range(n):
                if [i,j] in lines[0:l]:
                    grid[i][j] = '#'

                else:
                    search.append((i,j))

        # print_map(grid)

        dist = [100000000000000 for i in range(n*m)]
        prev = [None for i in range(n*m)]

        dist[0] = 0

        dir = [(-1,0),(0,1),(1,0),(0,-1)]

        while search:

            search = sorted(search, key=lambda idx: dist[idx[0]*m+idx[1]])

            u = search.pop(0)

            for d in dir:
                nx, ny = u[0]+d[0], u[1]+d[1]

                if nx in range(0,m) and ny in range(0,n):
                    if grid[nx][ny] != '#':
                        alt = dist[u[0]*m+u[1]]+1

                        if alt < dist[nx*m+ny]:
                            dist[nx*m+ny] = alt
                            prev[nx*m+ny] = u



        count = 0
        p = ex*m+ey

        if prev[p] != None:
            break

        l -= 1

    print(l)





