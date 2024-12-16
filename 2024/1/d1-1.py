def import_numbers(string):
    list = [[] for _ in range(2)]
    split_str = string.split("\n")
    for entry in split_str:
        entry = entry.split(" ")
        list[0].append(int(entry[0]))
        list[1].append(int(entry[-1]))
    return list

def score(list):
    list[0].sort()
    list[1].sort()

    dist = 0
    for i in range(len(list[0])):
        dist += abs(list[0][i] - list[1][i])
    return dist


with open("test.txt") as test:
    string = test.read()
    test_list = import_numbers(string)
    # print(test_list[0])
    # print(test_list[1])
    finalscore = score(test_list)
    print(finalscore)
