n = int(input())
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print('Осталось секунд:', (j - 1))
    print('Пуск', i)
