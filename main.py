max_count = int(input())
count_error = 0
countdown_end = 0
count = 1
while max_count > count_error:
    countdown = str(input())
    if count == 1 and countdown == 'раз':
        count += 1
        countdown_end += 1
    elif count == 2 and countdown == 'два':
        count += 1
        countdown_end += 1
    elif count == 3 and countdown == 'три':
        count += 1
        countdown_end += 1
    elif count == 4 and countdown == 'четыре':
        count = 1
        countdown_end += 1
    else:
        count_error += 1
        print('Правильных отсчётов было ', countdown_end, sep='', end='')
        print(', но теперь вы ошиблись.')
        count = 1
        countdown_end = 0
    if max_count <= count_error:
        print('На сегодня хватит.')
        break
