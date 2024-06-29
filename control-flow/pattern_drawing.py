pattern = int(input("Enter the size of the pattern: "))
Opattern = pattern
while pattern != 0:

    pattern -= 1
    for n in range(Opattern):
        print("*", end="")

    print()
