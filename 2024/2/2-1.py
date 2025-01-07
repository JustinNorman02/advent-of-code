
def data_intake(string):
    data = string.split("\n")
    return [[int(num) for num in line.split()]for line in data]


def check_safety(data):
    
    safe = 0

    for report in data:
        if report[0] - report[1] > 0:
            incdec = 1
        else:
            incdec = -1
        for entry in range(len(report)-1):
            change = report[entry] - report[entry+1]
            if (abs(change) > 3) | (abs(change) < 1) :
                break

            if change/abs(change) != incdec:
                break;

            if entry == len(report)-2:
                safe += 1

    return safe

with open("data.txt") as datastring:
    data = data_intake(datastring.read())
    safe = check_safety(data)
    print(safe)
    
