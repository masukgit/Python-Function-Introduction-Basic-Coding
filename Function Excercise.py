numbers = [1,2,4,6]

def multiplying_list(list):
    result = 1
    for number in list:
        result *= number
    return result

result = multiplying_list(numbers)

print(result)

def check_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for n in range(2, number):
            if number % n == 0:
                return False
            else:
                return True
print(check_prime(3))
