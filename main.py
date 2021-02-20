count_number = int(input())
list = []
list_number = []
for i in range(count_number):
    name = str(input())
    list.append(name)
    if name[-1] == '4' or name[-1] == '5':
        list_number.append(name)
for i in range(count_number):
    print(list[i])
print('')
for i in range(len(list_number)):
    print(list_number[i])
