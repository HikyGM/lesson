text = str(input())
count = max_count = 0
for i in range(len(text)):
    if text[i] == 'о':
        count += 1
        if count > max_count:
            max_count = count
    elif text[i] == 'р':
        count = 0
print(max_count)
