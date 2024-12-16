fileinput = open("data.txt", "r").read()

letters = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

rucksacks = fileinput.splitlines()
score = 0
common = []
for sack in rucksacks:
    compartment1, compartment2 = sack[:len(sack)//2], sack[len(sack)//2:]

    for letter in compartment1:
        if compartment2.__contains__(letter):
            common.append(letter)
            break;

for letter in common:
    score += letters.index(letter)

print(score)