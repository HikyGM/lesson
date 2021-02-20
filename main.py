text1 = str(input())
text2 = str(input())
count_bull = 0
count_cow = 0
for i in range(len(text1)):
    if text1[i] == text2[i]:
        count_bull += 1
    elif text2[i] in text1:
        count_cow += 1
print(count_bull, count_cow)