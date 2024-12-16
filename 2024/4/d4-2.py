
def check(string):

    lines = string.split('\n')
    m = len(lines)
    n = len(lines[0])

    xmas = 0
    for i in range(m):
        for j in range(n):
                xmas += check_xmas(lines,i,j,m,n)

    return xmas


    
def check_xmas(lines, i, j, m, n):
    if lines[i][j] != 'A':
        return False

    if not (1 <= i < m-1 and 1 <= j < n-1):
         return False

    top = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
    bot = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"


    if top in ["SM","MS"] and bot in ["SM", "MS"]:
         return True
   
    return False

    

    





with open('data.txt') as f:
    print(check(f.read()))