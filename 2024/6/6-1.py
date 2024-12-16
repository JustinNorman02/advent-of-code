 
def find_indicies(l, t):
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] == t:
                return y, x

    return -1, -1

def print_table(l):
    for row in l:
        print(" ".join(map(str, row)))

with open("data.txt") as f:
    lines = f.read().split()

    dir = [[-1,0],[0,1],[1,0],[0,-1]]

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    gy, gx = find_indicies(lines, '^')
    


    d = 0
    move = dir[d]
    ans = 1

    nexty = gy + move[0]
    nextx = gx + move[1]

    while 0<= nexty < len(lines) and 0 <= nextx < len(lines[0]):

        if lines[nexty][nextx] == '#':
            d = (d+1) % 4
            move = dir[d]

        if lines[gy][gx] != 'X':
            lines[gy][gx] = 'X'
            ans += 1
        

        gy = gy + move[0]
        gx = gx + move[1]

        nexty = gy + move[0]
        nextx = gx + move[1]

        # print_table(lines)


print_table(lines)

print(ans)



