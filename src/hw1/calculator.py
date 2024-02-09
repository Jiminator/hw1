from backend.api import add, subtract, divide, multiply


def calculator():  
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operation == '+':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '-':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '*':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '/':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Invalid operation. Please try again.")
    
    



