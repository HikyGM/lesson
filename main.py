bool_fra = False
count = 0
count2 = 0
fr = ''
while fr != 'СТОП':
    fr = str(input())
    fra = fr.lower()
    if not bool_fra:
        count += 1
    if 'кот' in fra:
        bool_fra = True
        count2 += 1
        continue
if bool_fra:
    print(count2, count)
elif not bool_fra:
    print('0 -1')
