n = int(input())
arr = set()
b = False
for i in range(n + 1):
    sity_name = str(input())
    if sity_name in arr:
        b = True
        print('TRY ANOTHER')
        break
    else:
        arr.add(sity_name)
if not b:
    print('OK')
