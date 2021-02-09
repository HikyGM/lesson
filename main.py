bool_fra = False
count = 0
fr = ''
while fr != 'СТОП':
    fr = str(input())
    fra = fr.lower()
    count += 1
    if 'кот' in fra:
        bool_fra = True
        print(count)
        break
if not bool_fra:
    print('-1')
