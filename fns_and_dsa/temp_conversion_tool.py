FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = float((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = float((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)
    return fahrenheit


def main():
    try :
        Temperature = float(input("Enter the temperature to convert: "))
        c_or_f = (
            input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        )
        if c_or_f == "C":
            result = convert_to_fahrenheit(Temperature)
            print(f"{Temperature} is {result}°F")
        elif c_or_f == "F":
            result = convert_to_celsius(Temperature)
            print(f"{Temperature} is {result}°F")
        else:
            print("invalid option")

    except ValueError :
        print("Invalid temperature. Please enter a numeric value.")            


if __name__ == "__main__":
    main()
