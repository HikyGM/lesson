result = str(input())
number_of_positions = int(result[:3])
the_amount = int(result[4:])
error_list = []
summa = 0
for i in range(number_of_positions):
    string = str(input())
    price_product = int(string[:6])
    count_products = int(string[8:11])
    result_price_products = int(string[13:])
    summa = summa + (price_product * count_products)
    if price_product * count_products != result_price_products:
        error_list.append(i)
n = the_amount - summa
if abs(n) == 0:
    print(n)
else:
    print(n)
    for i in range(len(error_list)):
        print(error_list[i] + 1, end=' ')
