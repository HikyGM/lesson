number_of_string = int(input())
white_list = []
allowed_request = []
for i in range(number_of_string):
    string = str(input())
    white_list.append(string)
number_of_search = int(input())
for i in range(number_of_search):
    string = str(input())
    if string in white_list:
        allowed_request.append(string)
for i in range(len(allowed_request)):
    print(allowed_request[i])
