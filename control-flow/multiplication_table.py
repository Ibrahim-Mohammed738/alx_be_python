number = float(input("Enter a number to see its multiplication table: "))

nums = range(1, 11)

for num in nums:
    print(f"{number} * {num} = {num * number}")
