number_of_string = int(input())
list_number = []
for i in range(number_of_string):
    number = int(input())
    list_number.append(number)
for i in range(number_of_string - 1):
    print(list_number[i] + list_number[i + 1])
