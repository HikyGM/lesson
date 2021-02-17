a = str(input())
b = str(input())
while a[-1] == b[0]:
    a = b
    b = str(input())
else:
    print(b)
