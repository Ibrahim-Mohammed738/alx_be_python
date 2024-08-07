def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            addItem = input("Enter the item to add: ").strip().lower()
            shopping_list.append(addItem)
            print(f"{addItem} added")
        elif choice == "2":
            RMitem = input("Enter the item to remove : ").strip().lower()
            if RMitem in shopping_list:
                shopping_list.remove(RMitem)
                print(f"{RMitem} removed")
            else:
                print("item not found")
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
