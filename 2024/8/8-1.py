import numpy

def print_square_with_hash(list, indices_to_replace):
    
    for i,j in indices_to_replace:
        # if list[i][j] == '.':
        list[i][j] == '#'

    for rows in list:
        print(''.join(rows))



with open('data.txt') as f:
    lines = f.read().split("\n")

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    n = len(lines)
    m = len(lines[0])
    indices = [(i, j) for i, sublist in enumerate(lines) for j, char in enumerate(sublist) if char != '.']
    # dirs = [[-1,0],[0,1],[1,0],[0,-1],[-1,1],[-1,-1],[1,-1],[1,1]]
    antinodes = []

    for p,(i,j) in enumerate(indices):
        antenna = lines[i][j]

        for k,l in indices[p+1:]:
            if lines[k][l] == antenna:
                dx, dy = k-i, l-j

                # print("[%d,%d]->[%d,%d]: %d by %d" %(i,j,k,l,dx,dy))
                # print(" Antinode 1: [%d, %d]" % (i-dx, j-dx))
                # print(" Antinode 2: [%d, %d]" % (k+dx, l+dx))

                print("")

                if i-dx in range(n) and j-dy in range(m) and [i-dx, j-dy] not in antinodes:
                    antinodes.append([i-dx, j-dy])
                    
                if k+dx in range(n) and l+dy in range(m) and [k+dx, l+dy] not in antinodes:
                    antinodes.append([k+dx,l+dy])


    # print_square_with_hash(lines, antinodes)
    print(len(antinodes))

