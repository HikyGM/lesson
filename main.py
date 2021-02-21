spisok = []
n = list(input().split(':'))
while n != ['']:
    spisok.append(n)
    n = list(input().split(':'))
c = list(input().split(';'))
for i in range(len(spisok)):
    if c.count(spisok[i][1]) != 0:
        print('To:', spisok[i][0])
        m = spisok[i][4].split(',')
        print(m[0] + ',' + ' ваш пароль слишком простой, смените его.')
