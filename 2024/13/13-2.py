import numpy as np
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
        
        ans = [ans[0]+ 10000000000000, ans[1]+10000000000000]

        A = [[a[0],b[0]],[a[1],b[1]]]
        
        x,y = np.linalg.solve(A,ans)
        
        x = round(x)
        y = round(y)

        if x*a[0] + y*b[0] == ans[0] and x*a[1] + y*b[1] == ans[1]:
            total += 3*x+y

        print(3*x+y)

    print(total)