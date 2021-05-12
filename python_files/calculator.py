def add(value_1, value_2):
    """this function adds two numbers together"""
    sum = value_1 + value_2
    return sum

def subtraction(value_1, value_2):
    difference = value_1 - value_2
    return difference


def multiplication(value_1, value_2):
    product = value_1 * value_2
    return product

def division(value_1, value_2):
    quotient = value_1 / value_2
    return quotient

a = float(input("Enter value one: "))
b = float(input("Enter value two: "))

print(add(a, b))
print(subtraction(a, b))
print(multiplication(a, b))
print(division(a, b))