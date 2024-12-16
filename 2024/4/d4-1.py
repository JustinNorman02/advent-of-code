
def check(string):
    dir = []
    lines = string.split('\n')
    m = len(lines)
    n = len(lines[0])

    for x in range(-1,2):
        for y in range(-1,2):
            if x != 0 or y != 0:
                dir.append([x,y])

    xmas = 0
    for i in range(m):
        for j in range(n):
            for d in dir:
                xmas += check_xmas(lines,i,j,d,m,n)

    return xmas


    
def check_xmas(lines, i, j, d, m, n):
    dx, dy = d
    
    for k, x in enumerate('XMAS'):
        ii = i + k * dx
        jj = j + k * dy

        if not (0 <= ii < m and 0 <= jj < n):
            return False
        if lines[ii][jj] != x:
            return False
    return True 





with open('data.txt') as f:
    print(check(f.read()))