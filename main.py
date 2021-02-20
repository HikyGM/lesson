number_of_string = int(input())
list_of_strings = []
search_string = []
for i in range(number_of_string):
    string = str(input())
    list_of_strings.append(string)
search_bar = str(input())
for i in range(number_of_string):
    if search_bar in list_of_strings[i]:
        print(list_of_strings[i])
