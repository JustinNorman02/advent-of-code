import re

def print_room(room):

    for line in room:
        print("".join(str(line)))


def simulate(room, bots):

    for bot in bots:
        nx, ny = (bot[0][0] + bot[1][0]) % h, (bot[0][1] + bot[1][1]) % w

        room[nx][ny] = room[nx][ny]+1

        room[bot[0][0]][bot[0][1]] = room[bot[0][0]][bot[0][1]]-1

        bot[0][0], bot[0][1] = nx, ny

    return room, bots

def score(quad):
    return sum(sum(lines) for lines in quad)


with open('data.txt') as f:
    lines = f.read()

    pattern = r'p=(-?\d+),(\d+) v=(-?\d+),(-?\d+)'
    
    # Find all matches in the input string
    matches = re.findall(pattern, lines)

    bots = [[[int(x),int(y)],[int(vx),int(vy)]] for x,y,vx,vy in matches]

    h = 101
    w = 103

    room = [[0 for _ in range(w)] for _ in range(h)]

    for bot in bots:
        room[bot[0][0]][bot[0][1]] = room[bot[0][0]][bot[0][1]]+1

    steps = 100

    for i in range(steps):    
        room, bots = simulate(room,bots)

    q1 = [row[:w//2] for row in room[:h//2]]
    q2 = [row[(w//2)+1:] for row in room[:h//2]]
    q3 = [row[:w//2] for row in room[(h//2)+1:]]
    q4 = [row[(w//2)+1:] for row in room[(h//2)+1:]]

    
    quad1 = score(q1)
    quad2 = score(q2)
    quad3 = score(q3)
    quad4 = score(q4)

    # print_room(room)

    print(quad1,quad2,quad3,quad4,quad1*quad2*quad3*quad4)







    