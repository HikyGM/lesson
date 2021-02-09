n = int(input())
bool_fra = False
for i in range(n):
    fr = str(input())
    fra = fr.lower()
    if 'кот' in fra:
        bool_fra = True
    if bool_fra:
        print('МЯУ')
        break
if not bool_fra:
    print('НЕТ')
