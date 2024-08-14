# basic calculator to perform arithmetic operations

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print('Select operation: \n'
      '1. ADD \n'
      '2. SUB \n'
      '3. MUL \n'
      '4. DIV \n')

choice = int(input("Enter choice:"))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

match choice:
    case 1:
        print(add(number1, number2))
    case 2:
        print(subtract(number1, number2))
    case 3:
        print(multiply(number1, number2))
    case 4:
        print(divide(number1, number2))
    case _:
        print("Invalid choice. Select between 1-4.")
