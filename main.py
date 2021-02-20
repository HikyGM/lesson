count = int(input())
text = str(input())
for i in range(len(text)):

    if 1040 <= ord(text[i]) <= 1071:
        if (ord(text[i]) + count) > 1071:
            a = ord(text[i]) + count - 1072 + 1040
            print(chr(a), end='')
        else:
            a = ord(text[i]) + count
            print(chr(a), end='')
    if 1072 <= ord(text[i]) <= 1103:
        if (ord(text[i]) + count) > 1103:
            a = ord(text[i]) + count - 1104 + 1072
            print(chr(a), end='')
        else:
            a = ord(text[i]) + count
            print(chr(a), end='')
    if not 1040 <= ord(text[i]) <= 1103:
        print(text[i], end='')