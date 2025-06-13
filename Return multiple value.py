a = 32
b = 20
addition = a + b
subs = 1 - b

print(addition, subs)

a = 32
b = 20
def add_sus(a, b):
    """
    This will addition and substruction of two numbers
    :param a: First number
    :param b: Second number
    :return: It will return addition and substruction
    """
    addition = a + b
    subs = a - b
    return addition, subs

print(add_sus.__doc__)
print(add_sus(12, 10))

result = add_sus(25, 13)
print(type(result))