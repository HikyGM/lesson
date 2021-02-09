count = int(input())
bool_continent = bool(True)
for i in range(count):
    n = input()
    if n == 'С кем война?':
        if bool_continent:
            print('Евразия')
        elif not bool_continent:
            print('Остазия')
    elif n == 'С кем мир?':
        if not bool_continent:
            print('Евразия')
        elif bool_continent:
            print('Остазия')
    elif n == 'Меняем':
        if bool_continent:
            bool_continent = False
        elif not bool_continent:
            bool_continent = True
