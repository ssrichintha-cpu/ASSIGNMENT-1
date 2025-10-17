# task1.py

def basic_operations():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"

        # Displaying results
        print(f"Addition: {num1} + {num2} = {addition}")
        print(f"Subtraction: {num1} - {num2} = {subtraction}")
        print(f"Multiplication: {num1} * {num2} = {multiplication}")
        print(f"Division: {num1} / {num2} = {division}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    basic_operations()