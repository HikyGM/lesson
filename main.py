bf = input()
qwe = [0] * len(bf)
start = 0
for i in range(len(bf)):
    if bf[i] == '>':
        start += 1
    elif bf[i] == '<':
        start -= 1
    elif bf[i] == '+':
        if qwe[start] == 255:
            qwe[start] = 0
        else:
            qwe[start] += 1
    elif bf[i] == '-':
        if qwe[start] == 0:
            qwe[start] = 255
        else:
            qwe[start] -= 1
    elif bf[i] == '.':
        print(qwe[start])
