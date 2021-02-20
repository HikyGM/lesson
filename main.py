print(ord('А'))
print(ord('Я'))
print(ord('а'))
print(ord('я'))

count = int(input())
text = str(input())
for i in range(len(text)):
    if 1103 >= ord(text[i]) >= 1040:
        symbol = ord(text[i]) + count
        if 1103 >= symbol >= 1040:
            print(chr(symbol), end='')

    else:
        print(chr(ord(text[i])), end='')
