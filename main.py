text = str(input())
symbol = int(input())
text_complete = ' ' + text
if 0 < symbol < len(text_complete):
    print(text_complete[symbol])
else:
    print('ОШИБКА')