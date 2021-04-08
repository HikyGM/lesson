n = int(input())
m = int(input())
qwe = []
table = []
for i in range(n):
    for j in range(m):
        qwe.append(input())
    table.append(qwe)
    qwe = []
for row in table:
    print(*row, sep="\t")
