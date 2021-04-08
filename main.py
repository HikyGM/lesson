n = input().split(' ')
n.insert(0, '0')
m = input().split(' ')
m.insert(0, '0')
for i in range(1, len(n)):
    if i == 1:
        print(m[int(n[i])].capitalize(), end=' ')
    else:
        print(m[int(n[i])].lower(), end=' ')
