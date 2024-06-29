Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no):  ")
Priority = input("Priority (high/medium/low): ")

match Priority:
    case "high":
        print(f"Reminder: {Task}, is a high priority task", end="")

    case "medium":
        print(f"Note: {Task}, is a medium priority task", end="")

    case "low":
        print(f"Note: {Task}, is a low priority task", end="")

if Time_Bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(" Consider completing it when you have free time.")
