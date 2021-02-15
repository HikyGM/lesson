subsid = int(input())
count_skot = int(input())
for i in range(1, min(count_skot, subsid // 20) + 1):
    for j in range(0, min(count_skot, subsid // 10) + 1):
        for k in range(0, min(count_skot, subsid // 5) + 1):
            if i * 20 + j * 10 + k * 5 == subsid:
                if i + j + k == count_skot:
                    print(i, j, k)