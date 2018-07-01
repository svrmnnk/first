white_list_quantity = int(input("number of items in white list: "))

white_list = []

for i in range(white_list_quantity):
    white_list.append(input("type the word for the white list: "))

request_quantity = int(input("type the number of requests: "))

request_list = []

for i in range(request_quantity):
    request_list.append(input("type your requests: "))

for item in request_list:
    if item in white_list:
        print(item)