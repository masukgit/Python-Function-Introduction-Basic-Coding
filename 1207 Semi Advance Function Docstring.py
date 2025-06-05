def fahrenheit_celsius(fahrenheit):
    """
    This function will convert Fahrenheit to Celsius temperature
    :param fahrenheit: It takes Fahrenheit temperature as parameter
    :return: It will return Celsius temperature
    """
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
# print(fahrenheit_celsius(98.6))
print(fahrenheit_celsius.__doc__)
