import re

def extract_coordinates(input_string):
    # Regular expression to match patterns like X+94, Y+34 or X=8400, Y=5400
    pattern = r'X[=+](\d+),\s*Y[=+](\d+)'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    # Convert matches to a list of lists of integers
    coordinates = [[int(x), int(y)] for x, y in matches]
    
    return coordinates

with open('data.txt') as f:

    lines = f.read().split('\n\n')

    combos = [extract_coordinates(i) for i in lines]

    cost = [1,3]

    total = 0
    

    for a,b,ans in combos:
        pos = []
        for i in range(0,101):
            for j in range(0, 101):
                if i*a[0] + j*b[0] == ans[0] and i*a[1] + j*b[1] == ans[1]:
                    pos.append([i,j])

        val = 0
        for i,j in pos:
            if 3*i+j > val:
                val = 3*i+j

        total += val

        print(val)

    print(total)