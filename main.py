# n = int(input())
# m = int(input())
# e = int(input())
# for i in range(n, e, m):
#     print(i, end=' ')
#     if i == e - m:
#         print(e)

# strok = str(input())
# if (len(strok) <= 7) and (strok < 'флейта') and ('нота' not in strok) and ('до' or 'ля' in strok):
#     if 'до' or 'ля' in strok:
#         if len(strok) % 2 == 0:
#             print('МОЖЕТ')
#         else:
#             print('НЕ МОЖЕТ')
#     elif 'соль' in strok:
#         if len(strok) % 2 == 1:
#             print('МОЖЕТ')
#         else:
#             print('НЕ МОЖЕТ')
# else:
#     print('НЕ МОЖЕТ')

# count = 0
# text = str(input())
# while text != 'ВСЁ':
#     if 'Полуэкт' in text:
#         count += 1
#     elif 'Амбруаз' in text:
#         count += 1
#     text = str(input())
# print(count)

# n = int(input())
# count_strah = 0
# count_dobr = 0
# count_jadn = 0
# for i in range(n):
#     text = str(input())
#     if 'страх' in text:
#         count_strah += 1
#     elif 'доброта' in text:
#         count_dobr += 1
#     elif 'жадность' in text:
#         count_jadn += 1
# a = max(count_strah, count_jadn, count_dobr)
# print(a)
# if count_jadn == count_strah == count_dobr:
#     print('Доброта Жадность Страх')
# else:
#     if count_strah == a:
#         print('Страх', end=' ')
#         if count_jadn == count_dobr:
#             print('Доброта Жадность')
#         elif count_jadn > count_dobr:
#             print('Доброта Жадность')
#         elif count_jadn < count_dobr:
#             print('Жадность Доброта')
#     elif count_dobr == a:
#         print('Доброта', end=' ')
#         if count_jadn == count_strah:
#             print('Жадность Страх')
#         elif count_jadn > count_strah:
#             print('Жадность Страх')
#         elif count_jadn < count_strah:
#             print('Страх Жадность')
#     elif count_jadn == a:
#         print('Жадность', end=' ')
#         if count_jadn == count_dobr:
#             print('Доброта Страх')
#         elif count_dobr > count_strah:
#             print('Доброта Страх')
#         elif count_dobr < count_strah:
#             print('Страх Доброта')

# subsid = int(input())
# count_skot = int(input())
# for i in range(1, min(count_skot, subsid // 20) + 1):
#     for j in range(0, min(count_skot, subsid // 10) + 1):
#         for k in range(0, min(count_skot, subsid // 5) + 1):
#             if i * 20 + j * 10 + k * 5 == subsid:
#                 if i + j + k == count_skot:
#                     print(i, j, k)

text = str(input())
symbol = int(input())
text_complete = ' ' + text
if 0 < symbol < len(text_complete):
    print(text_complete[symbol])
else:
    print('ОШИБКА')