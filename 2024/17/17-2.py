from tqdm import tqdm


# with open("test.txt") as f:
with open("data.txt") as f:

    reg, ins = f.read().split("\n\n")

    instr = ins

    ins = ins.split()[1].split(',')

    for i in range(len(ins)):
        ins[i] = int(ins[i])

    reg = reg.split('\n')

    regs = [0,0,0]
    
    regs[0] = int(reg[0].split()[2])
    regs[1] = int(reg[1].split()[2])
    regs[2] = int(reg[2].split()[2])

    insp = 0

    out = ""

    for i in tqdm(range(100000000000000,100000000000000000)):

        regs[0] = i

        while 0 <= insp < len(ins):

            op = ins[insp]

            inp = ins[insp+1] 

            if op == 0:
                if inp == 4:
                    inp = regs[0]

                elif inp == 5:
                    inp = regs[1]
                    
                elif inp == 6:
                    inp = regs[2]

                elif inp == 7:
                    raise RuntimeError


                regs[0] = regs[0] // 2**(inp)

            elif op == 1:
                regs[1] = regs[1] ^ inp

            elif op == 2:
                if inp == 4:
                    inp = regs[0]

                elif inp == 5:
                    inp = regs[1]
                    
                elif inp == 6:
                    inp = regs[2]

                elif inp == 7:
                    raise RuntimeError

                regs[1] = inp % 8

            elif op == 3:
                if regs[0]:
                    insp = inp
                    continue

            elif op == 4:
                regs[1] = regs[1]^regs[2]

            elif op == 5:
                if inp == 4:
                    inp = regs[0]

                elif inp == 5:
                    inp = regs[1]
                    
                elif inp == 6:
                    inp = regs[2]

                elif inp == 7:
                    raise RuntimeError

                if out:
                    out += ","

                out += str(inp%8)
                

            elif op == 6:
                if inp == 4:
                    inp = regs[0]

                elif inp == 5:
                    inp = regs[1]
                    
                elif inp == 6:
                    inp = regs[2]

                elif inp == 7:
                    raise RuntimeError


                regs[1] = regs[0] // 2**(inp)

            elif op == 7:
                if inp == 4:
                    inp = regs[0]

                elif inp == 5:
                    inp = regs[1]
                    
                elif inp == 6:
                    inp = regs[2]

                elif inp == 7:
                    raise RuntimeError


                regs[2] = regs[0] // 2**(inp)
            
            insp += 2

        if out == instr:
            print(i)
            break







 
