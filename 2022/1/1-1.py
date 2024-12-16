elvestring = open('data.txt', 'r').read()

elveint = elvestring.splitlines()


last = 0
elves = [0]
for line in elveint:
    if not line:
        last += 1
        elves.append(0)

    else:
        value = int(line)
        elves[last] += value

elves.sort()

top3 = elves[last]+elves[last-1]+elves[last-2]
print(top3)



