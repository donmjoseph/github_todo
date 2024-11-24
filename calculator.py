# calculator.py

def calculator():
    print("Basic Calculator")
    print("Options:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    while True:
        try:
            # Get user choice
            choice = input("Choose an option (1-5): ")
            if choice == '5':
                print("Goodbye!")
                break

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please choose a valid option.")
                continue

            # Get numbers from the user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform the calculation
            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The result is: {num1 / num2}")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    calculator()

