
def data_intake(string):
    data = string.split("\n")
    return [[int(num) for num in line.split()]for line in data]


def check_safety(data):
    
    safe = 0

    for report in data:
        good = False
        for j in range(len(report)):
            subreport = report[:j] + report[j+1:]
            incdec = (subreport == sorted(subreport) or subreport == sorted(subreport, reverse=True))
            ok = True
            for i in range(len(subreport)-1):
                change = abs(subreport[i]-subreport[i+1])
                if not 1<=change<=3:
                    ok = False

            if incdec & ok:
                good = True

        if good:
            safe += 1


    return safe

with open("data.txt") as datastring:
    data = data_intake(datastring.read())
    safe = check_safety(data)
    print(safe)
    
