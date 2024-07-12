def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"The result of the division is {result}")

    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    except ValueError:
        print(f"Error: Please enter numeric values only.")
    except TypeError:
        print(f"Error: Please enter numeric values only.")
