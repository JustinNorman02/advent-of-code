import re

def parse(string):
    ans = 0
    string = re.sub("don't.*?(?=do|$)",'', string, flags=re.DOTALL) #Part 2
    x = re.findall("mul\((-?\d+),(-?\d+)\)", string) #Part 1
    # print(x)
    for match in x:
        ans += int(match[0])*int(match[1])
    return ans

with open('data.txt') as f:
    print(parse(f.read()))