count_number = int(input())
list = []
for i in range(count_number):
    name = int(input())
    list.append(name)
for i in range(count_number - 1):
    for j in range(count_number - 1 - i):
        if list[j] < list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
        elif list[j] == list[j + 1]:
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
for i in range(count_number):
    print(list[i])
