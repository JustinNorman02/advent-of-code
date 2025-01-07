def move(sx,sy,tx,ty):
    mx,my = tx-sx, ty-sy

    path = ""

    if mx < 0:
            for i in range(abs(mx)):
                path += '^'
        
    else:
        for i in range(abs(mx)):
            path += 'v'

    if my < 0:
        for i in range(abs(my)):
            path += '<'
    
    else:
        for i in range(abs(my)):
            path += '>'


    path += 'A'

    return path


def keypad_path(code, pad):
    path = ""

    sx,sy = pad['A']

    for entry in code:
        tx,ty = pad[entry]

        path += move(sx,sy,tx,ty)

        sx,sy = tx,ty

        


    return path

def path_control(code, pad):

    sx,sy = pad['A']

    path = ""

    code_snip = code.split('A')

    for u in range(len(code_snip)):
        code_snip[u] = list(code_snip[u])

    
    for entry in code_snip:

        if entry:
            while entry:

                # entry = sorted(entry, key = lambda x: abs(pad[x][0]-sx)+abs(pad[x][1]-sy))

                tx,ty = pad[entry.pop(0)]

                path += move(sx,sy,tx,ty)

                sx,sy = tx,ty

            tx,ty = pad['A']

            path += move(sx,sy,tx,ty)

            sx,sy = tx,ty

        
    return path

with open("test.txt") as f:
# with open("data.txt") as f:

    lines = f.read().split("\n")


    kp = [['7','8','9'],['4','5','6'],['1','2','3'],['','0','A']]

    keypad = {}

    for i in range(len(kp)):
        for j in range(len(kp[0])):
            keypad[kp[i][j]] = (i,j)

    c = [['','^','A'],['<','v','>']]

    control = {}

    for i in range(len(c)):
        for j in range(len(c[0])):
            control[c[i][j]] = (i,j)


    print(control)

    ans = 0

    for entry in lines:
        num = int(''.join([i for i in entry if i.isdigit()]))

        path = keypad_path(keypad_path(keypad_path(entry,keypad),control),control)
       
        print(entry,len(path),num,path)

        ans += len(path)*num
        print(ans)

    print(ans)

