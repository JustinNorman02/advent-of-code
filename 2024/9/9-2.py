def convert_to_disk(diskmap):

    disk = []
    filelen = []

    fid = 0

    for i in range(len(diskmap)):
        if i % 2 == 0:
            for _ in range(int(diskmap[i])):
                disk.append(str(fid))
            fid += 1
            filelen.append(int(diskmap[i]))

        else:
            for _ in range(int(diskmap[i])):
                disk.append('.')

    return disk, filelen

def checksum(disk):
    ans = 0

    for i in range(len(disk)):
        if disk[i] == '.':
            continue

        ans += int(disk[i]) * i

    return ans


with open('data.txt') as f:

    disk, filelen = list(convert_to_disk(f.read()))

    spaces = {}
    i = 0
    while i < len(disk):

        empty = 0
        start = 0

        if disk[i] == '.':
            start = i
            while disk[i] == '.':
                empty += 1
                i += 1
            
            spaces[start] = empty
        else:
            i += 1



    i = len(filelen)-1

    while i >= 0:
        print(i)

        pstart = disk.index(str(i))

        for key in spaces:
            val = spaces[key]
            if key >= pstart:
                filelen.pop()
                i -= 1
                break 

            if 0 < filelen[i] <= val:
                for j in range(filelen[i]):
                    disk[key+j], disk[pstart+j] = disk[pstart+j], disk[key+j]

                spaces.pop(key)

                if filelen[i] < val:
                    spaces[key+filelen[i]] = val-filelen[i]
                
                if pstart-1 > 0 and disk[pstart-1] == '.' and pstart + filelen[i] < len(disk) and disk[pstart + filelen[i]] == '.':
                    newlen = filelen[i] + spaces[pstart + filelen[i]]

                    spaces.pop(pstart + filelen[i])

                    k = 1

                    while pstart - k > 0 and disk[pstart-k] == '.':
                        k += 1

                    newlen += spaces[pstart-k+1]

                    spaces[pstart-k+1] = newlen


                elif pstart-1 > 0 and disk[pstart-1] == '.':
                    k = 1

                    while pstart - k > 0 and disk[pstart-k] == '.':
                        k += 1

                    spaces[pstart-k+1] += filelen[i]

                elif pstart + filelen[i] < len(disk) and disk[pstart + filelen[i]] == '.':
                    spaces[pstart] = filelen[i] + spaces[pstart + filelen[i]]

                    spaces.pop(pstart + filelen[i])


                else:
                    spaces[pstart] = filelen[i]

                filelen.pop()
                i -=1

                spaces = {key: spaces[key] for key in sorted(spaces)}

                break




        
            
            


    print(disk)
    print(checksum(disk))
