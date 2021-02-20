count_string = int(input())
for i in range(count_string):
    string = str(input())
    if string[:2] == '%%':
        string = string[2:]
    elif string[:4] == '####':
        continue
    print(string)
