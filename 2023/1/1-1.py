with open('./data.txt', 'r') as file:
    string = file.read()
#
    string_list = string.split('\n')
    total = 0

number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

for line in string_list:
    word = ''
    first_digit = None
    last_digit = None
    for char in line:
        word += char
        if char.isdigit():
            if first_digit == None:
                first_digit = char
            last_digit = char

        else:
            for i in range(len(word) - 2):
                if word[i:] in number:
                    if first_digit == None:
                        first_digit = str(number.index(word[i:])+1)
                    last_digit = str(number.index(word[i:])+1)
                    word = ''

    total += int(first_digit + last_digit)

print(total)
