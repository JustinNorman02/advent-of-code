def convert_to_disk(diskmap):

    disk = []
    fid = 0

    for i in range(len(diskmap)):
        if i % 2 == 0:
            for _ in range(int(diskmap[i])):
                disk.append(str(fid))
            fid += 1

        else:
            for _ in range(int(diskmap[i])):
                disk.append('.')

    return disk

def checksum(disk):
    ans = 0

    for i in range(len(disk)):
        if disk[i] == '.':
            break

        ans += int(disk[i]) * i

    return ans


with open('data.txt') as f:

    disk = list(convert_to_disk(f.read()))

    i = 0
    j = len(disk)-1

    while i < j:
        
        if disk[i] == '.':
            if disk[j] == '.':
                j -= 1
                continue
            else:
                disk[i], disk[j] = disk[j], disk[i]
    
        i += 1

    
    print(checksum(disk))
