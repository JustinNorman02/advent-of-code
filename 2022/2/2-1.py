fileinput = open("data.txt", "r").read()

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
TIE = 3
WIN = 6

split = fileinput.splitlines()
score = 0
for i, string in enumerate(split):
    split[i] = string.split(' ')

    if split[i][0] == 'A':
        if split[i][1] == 'Y':
            score += TIE + ROCK
        if split[i][1] == 'Z':
            score += WIN + PAPER
        if split[i][1] == 'X':
            score += LOSE + SCISSORS

    if split[i][0] == 'B':
        if split[i][1] == 'X':
            score += LOSE + ROCK
        if split[i][1] == 'Y':
            score += TIE + PAPER
        if split[i][1] == 'Z':
            score += WIN + SCISSORS

    if split[i][0] == 'C':
        if split[i][1] == 'Z':
            score += WIN + ROCK
        if split[i][1] == 'X':
            score += LOSE + PAPER
        if split[i][1] == 'Y':
            score += TIE + SCISSORS

print(score)