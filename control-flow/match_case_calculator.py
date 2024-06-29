num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation_tybe = input("Choose the operation (+, -, *, /): ")

match operation_tybe:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2

print(f"The result is {result}")
