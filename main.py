n = int(input())
m = int(input())
x = False
while m != 0:
    if not x:
        if n < m:
            a = m
            x = True
    if x:
        if n > m:
            b = m
            break
    n = m
    m = int(input())
print(a, b, b - a)
