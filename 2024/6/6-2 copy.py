import copy

def find_indicies(l, t):
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] == t:
                return y, x

    return -1, -1

def print_table(l):
    for i in range(len(l)):
        print(" ".join(map(str, l[i])))
    print()    

def simulate(l):
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    gy, gx = find_indicies(l, '^')
    
    d = 0
    move = dir[d]

    nexty = gy + move[0]
    nextx = gx + move[1]
    
    seen = set()

    while nexty in range(len(l)) and nextx in range(len(l[0])):

        if (gy,gx,d) in seen:
            return seen, True
        
        seen.add((gy,gx,d))

        while l[nexty][nextx] == '#':
            d = (d+1) % 4
            move = dir[d]
            nexty = gy + move[0]
            nextx = gx + move[1]

        gy = gy + move[0]
        gx = gx + move[1]

        nexty = gy + move[0]
        nextx = gx + move[1]
    
    return seen, False

with open("data.txt") as f:
    lines = f.read().split()

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    ans = 0
    add = []


    # temp_lines = copy.deepcopy(lines)
    # temp_lines[4][5] = '#'
    # simulate(temp_lines)

    seen, res  = simulate(lines)

    print(res)


    for entry in list(seen):
        i, j, _ = entry

        if [i,j] in add:
            continue

        if lines[i][j] != '^' and lines[i][j] != '#':
            lines[i][j] = '#'

            _, res = simulate(lines)           

            if res == True:
                ans += 1
                add.append([i,j])

            lines[i][j] = '.'



# print_table(lines, [[] for line in lines])
print(ans)


