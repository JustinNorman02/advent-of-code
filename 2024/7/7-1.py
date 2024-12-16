import itertools


def evaluate(num, ops):
    exp = num[0]

    for i in range(1, len(num)):

        if ops[i-1] != "||":
            exp += ' ' + ops[i-1] + ' ' + num[i]
        else:
            exp += num[i]

        exp = eval(exp)
        exp = str(exp)

    return int(exp)

with open('data.txt') as f:

    lines = f.read().split('\n')

    for i in range(len(lines)):
        lines[i] = lines[i].split(": ")
        lines[i][1] = lines[i][1].split()

    ans = 0
    
    for i, line in enumerate(lines):
        print(i)
        res = int(line[0])
        nums = line[1]

        n = len(nums)

        if not n == 1:
            operations = ["*", "+", "||"]

            ops_combo = list(itertools.product(operations, repeat=n-1))

            for ops in ops_combo:
                if evaluate(nums, ops) == res:
                    ans += res
                    break

    print(ans)
