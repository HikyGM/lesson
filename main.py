number_of_products = int(input())
list_of_products = []
for i in range(number_of_products):
    name_products = str(input())
    list_of_products.append(name_products)
for i in range(number_of_products):
    print(list_of_products[i])
