from math import floor

def mix(sec,num):
    return sec^num

def prune(sec):
    return sec % 16777216

def next_sec(sec):
    p1 = sec * 64
    sec = prune(mix(sec,p1))

    p2 = floor(sec / 32)
    sec = prune(mix(sec,p2))

    p3 = sec * 2048
    sec = prune(mix(sec,p3))

    return sec



    





# with open("test.txt") as f:
with open("data.txt") as f:

    lines = f.read().split("\n")

    for i in range(len(lines)):
       lines[i] = int(lines[i])

    ans = 0

    for sec in lines:
        for i in range(2000):

            sec = next_sec(sec)

        ans += sec
        print(sec)

    print(ans)

    
