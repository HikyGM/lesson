count_string = int(input())
list_spisok = []
for i in range(count_string):
    spisok = str(input())
    if 'лук' in spisok:
        continue
    list_spisok.append(spisok)
print(', '.join(list_spisok))
