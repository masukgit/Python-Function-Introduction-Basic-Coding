num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 67, 98, 100]
num_list2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 211, 213, 215, 267, 298, 2100]

# even_num_list = []
# for number in num_list:
#     if number % 2 == 0:
#         even_num_list.append(number)
# print(even_num_list)

def even_num_finder(number_list):
    even_num_list = []
    for number in number_list:
        if number % 2 == 0:
            even_num_list.append(number)
    return even_num_list

even_list_one = even_num_finder(num_list)
even_list_two = even_num_finder(num_list2)

print(even_list_one)
print(even_list_two)