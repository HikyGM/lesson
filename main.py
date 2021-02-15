men = int(input())
men_works = []
for _ in range(men):
    men_works.append(input())
result = 0
for example in set(men_works):
    cout = 0
    for name in men_works:
        if example == name:
            cout += 1
    if cout > 1:
        result += cout
print(result)
