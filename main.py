qwe = []
for i in range(int(input())):
    n = input()
    qwe.append(n.split(','))
for i in range(int(input())):
    m = str(input())
    print(qwe[int(m[0])][int(m[2])])
