# def add (a, b):
#     return a + b
#
# def addition (a, b, c):
#     return a + b + c
#
# print(add(5, 7))
# print(addition(7, 3, 9))
#
# def multiple_addition(*number):
#     for x in number:
#         print(x)
# multiple_addition(2,2,1,5,4,8,9)

def multiple_addition(*number):
    sum = 0
    for x in number:
        sum += x
    return sum

print(multiple_addition(2,2,1,5,4,8,9))
