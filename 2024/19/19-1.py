import itertools

cache = {}

def solve(s):
    if s not in cache:
        if len(s) == 0:
            return 1
        else:
            result = 0
            for t in tow:
                if s.startswith(t):
                    result += solve(s[len(t):])
                cache[s] = result
    return cache[s]


# with open("test.txt") as f:
with open("data.txt") as f:

    tow , pat = f.read().split("\n\n")

    tow = tow.split(', ')

    pat = pat.split('\n')

    #for i in range(len(lines)):
    #    lines[i] = list(lines[i])

    possible = 0

    for p in pat:
        solve(p)

        if cache[p] > 0:
            possible += cache[p]


    print(possible)


    
        
