import itertools

# with open("test.txt") as f:
with open("data.txt") as f:

    lines = f.read().split("\n")

    computers = {}

    for i in range(len(lines)):
        lines[i] = lines[i].split('-')

        if lines[i][0] not in computers:
           computers[lines[i][0]] = [lines[i][1]]

        else:
            if lines[i][1] not in computers[lines[i][0]]: 
                computers[lines[i][0]].append(lines[i][1])

        if lines[i][1] not in computers:
           computers[lines[i][1]] = [lines[i][0]]

        else:
            if lines[i][0] not in computers[lines[i][1]]: 
                computers[lines[i][1]].append(lines[i][0])


    triples = []

    for c, adj in computers.items():

        for c2 in adj:
            adj2 = computers[c2]

            for c3 in adj2:
                adj3 = computers[c3]

                if c in adj3 and not any(comb in triples for comb in itertools.permutations((c,c2,c3))):
                    if 't' == c[0] or 't' == c2[0] or 't' == c3[0]:
                        triples.append((c,c2,c3))

    print(len(triples))
