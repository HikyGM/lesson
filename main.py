count_number = int(input())
list_number = []
log = False
for i in range(count_number):
    list_number.append(int(input()))
number = int(input())
for i in range(len(list_number) - 1):
    for j in range(i + 1, len(list_number)):
        if list_number[i] * list_number[j] == number:
            log = True
            break
if log:
    print('ДА')
else:
    print('НЕТ')
