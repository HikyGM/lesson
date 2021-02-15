m = int(input())
n = int(input())
arr_name = set()
for i in range(m + n):
    name = str(input())
    if name not in arr_name:
        arr_name.add(name)
    else:
        arr_name.remove(name)
if len(arr_name) != 0:
    print(len(arr_name))
else:
    print('NO')