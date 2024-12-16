

def search_values(value):
    return [key for key, value_list in rules_dict.items() if value in value_list]

with open("data.txt") as f:
    rules, updates = f.read().split("\n\n")

    rules = rules.split('\n')
    rules_dict = {}
    updates = updates.split('\n')
    
    for rule in rules:
        x, y = rule.split('|')

        if x in rules_dict:
            rules_dict[x].append(y)
        else:
            rules_dict[x] = [y]

    for i, update in enumerate(updates):
        updates[i] = update.split(',')

    ans = 0

    for update in updates:
        good = True
        for i, page in enumerate(update):
            before_rules = search_values(page)
            after_rules = []
            if page in rules_dict:
                after_rules = rules_dict[page]
            before = update[:i]
            after = update[i+1:]

            for entry in before:
                if entry in after_rules:
                    good = False
                    break

            for entry in after:
                if entry in before_rules:
                    good = False
                    break

        if good == True:
            ans += int(update[len(update)//2])
        

    print(ans)



