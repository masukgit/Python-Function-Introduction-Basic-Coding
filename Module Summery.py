def area(base, height):
    """
    This function will calculate the area of a triangle
    The formula is 0.5 * base * height
    :param base: base of the triangle
    :param height: height of the triangle
    :return: area of the triangle
    """
    area_cal = 0.5 * base * height
    return area_cal
print(area.__doc__)
print(area(7.2, 5.6))

def multiply(*numbers):
    sum = 1
    for number in numbers:
        sum *= number
    return sum
print(multiply(2, 6, 8))