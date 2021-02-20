count_drob = int(input())
a = 0
b = 0
for i in range(count_drob):
    n = int(input())
    m = int(input())
    if count_drob == 1:
        a = n
        b = m
    elif a == 0 and b == 0:
        a = n
        b = m
        continue
    a = (a * m) + (n * b)
    b = (m * b)
    ch = a
    zn = b
    q = a
    while zn % ch != 0:
        r = zn % ch
        zn, q, ch = ch, zn // ch, r
    b = b // ch
    if count_drob == 1:
        a = 1
        continue
    a = a // ch
print(a, '/', b, sep='')
