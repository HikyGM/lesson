n = int(input())
spisok = {}
count = 0
lis = []
for i in range(n):
    slovo = str(input())
    for j in range(len(slovo)):
        if slovo[j] == ' ':
            count = j
            break
        else:
            continue
    if slovo[count + 1:] in spisok:
        spisok[slovo[count + 1:]] = spisok[slovo[count + 1:]] + ' ' + slovo[:count]
    else:
        spisok[slovo[count + 1:]] = slovo[:count]
    count = 0
m = int(input())
for i in range(m):
    search = str(input())
    lis.append(search)
for i in range(len(lis)):
    if lis[i] in spisok:
        print(spisok[lis[i]])
    else:
        print('Нет в словаре')
