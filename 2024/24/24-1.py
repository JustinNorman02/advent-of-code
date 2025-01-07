# with open("test.txt") as f:
with open("data.txt") as f:

    inputs, ops = f.read().split("\n\n")



    wires = {}
    operations = []


    for ip in inputs.split('\n'):
        w, i = ip.split(': ')
        wires[w] = int(i)

    
    for entry in ops.split('\n'):
        entry = entry.split()
        operations.append([entry[0],entry[1],entry[2],entry[4]])

    outputs = {}

    while operations:
        op = operations.pop(0)

        i1 = wires[op[0]] if op[0] in wires else None

        if i1 is None:
            i1 = outputs[op[0]] if op[0] in outputs else None

        if i1 is None:
            operations.append(op)
            continue

        i2 = wires[op[2]] if op[2] in wires else None

        if i2 is None:
            i2 = outputs[op[2]] if op[2] in outputs else None

        if i2 is None:
            operations.append(op)
            continue

        if op[3] not in outputs:

            if op[1] == 'AND':
                outputs[op[3]] = i1 & i2

            elif op[1] == "OR":
                outputs[op[3]] = i1 | i2

            elif op[1] == 'XOR':
                outputs[op[3]] = i1 ^ i2

            else:
                raise Exception(op[1])
            


    zs = {}

    for k, v in outputs.items():
        if k[0] == 'z':
            zs[k] = v


    
    z = list(dict(sorted(zs.items(), reverse=True)).values())

    z = sum(j<<i for i,j in enumerate(reversed(z)))

    print(z)


    