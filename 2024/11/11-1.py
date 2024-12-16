from tqdm import tqdm

def blink(stones):
    new_stones = []

    for stone in stones:

        if stone == '0':
            new_stones.append('1')
            

        elif len(stone) % 2 == 0:
            new_stones.append(str(int(stone[:len(stone)//2])))
            new_stones.append(str(int(stone[len(stone)//2:])))

        else:
            new_stones.append(str(int(stone)*2024))

    return new_stones

cache = {}
def ans(x, n):

    x= int(x)

    if n == 0:
        return 1
    
    if (x,n) not in cache:
        if x == 0:
            result = ans(1, n-1)
        elif len(str(x)) % 2 == 0:
            x = str(x)
            mid = len(x) // 2
            result = ans(int(x[:mid]), n - 1) 
            result += ans(int(x[mid:]), n - 1)
            x = int(x)
        else:
            result = ans(x*2024, n-1)

        cache[(x,n)] = result
    
    return cache[(x, n)]



with open("data.txt") as f:
    stones = f.read().split()

    res = 0
    for x in stones:
        res += ans(int(x), 75)


    print(res)