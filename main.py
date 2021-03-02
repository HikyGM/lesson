inp = input().split(" ")
res = []
for a in inp:
    if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):  # !!!
        res.append(int(a))
    elif a == "+":
        a2 = res.pop()
        a1 = res.pop()
        res.append(a1 + a2)
    elif a == "-":
        a2 = res.pop()
        a1 = res.pop()
        res.append(a1 - a2)
    elif a == "*":
        a2 = res.pop()
        a1 = res.pop()
        res.append(a1 * a2)
    elif a == "/":
        a2 = res.pop()
        a1 = res.pop()
        res.append(a1 // a2)
    elif a == "~":
        a2 = res.pop()
        res.append(-a2)
    elif a == "#":
        a2 = res.pop()
        res.append(a2)
        res.append(a2)
    elif a == "@":
        a3 = res.pop()
        a2 = res.pop()
        a1 = res.pop()
        res.append(a2)
        res.append(a3)
        res.append(a1)
    elif a == "!":
        a1 = res.pop()
        p = 1
        for i in range(2, a1 + 1):
            p *= i
        res.append(p)
print(res[0])
