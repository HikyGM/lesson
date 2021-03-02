count_titul = int(input())
list_titul = []
for i in range(count_titul):
    titul = []
    name = str(input())
    while name != '*':
        titul += name.strip().split()
        name = str(input())
    list_titul.append('-'.join(titul))
    titul = []
print(', '.join(list_titul[::-1]))
